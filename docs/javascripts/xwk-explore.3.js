/* Explore visualizations — coverage matrix + mapping network */

(function () {
  const SOURCE_COLORS = {
    BFO: "#0f766e",
    DOLCE: "#1d4ed8",
    SUMO: "#b45309",
    UFO: "#7c3aed",
    GFO: "#be123c",
    YAMATO: "#047857",
    TUpper: "#0369a1",
    GUM: "#c2410c",
  };

  const RELATION_COLORS = {
    "close-match": "#0f766e",
    "exact-equivalence-candidate": "#065f46",
    overlap: "#1d4ed8",
    related: "#0369a1",
    "broader-than": "#7c3aed",
    "explicit-non-equivalence": "#be123c",
    unknown: "#64748b",
  };

  function siteRoot() {
    const match = location.pathname.match(/^(.*?)\/explore(?:\/|$)/);
    if (match) return match[1];
    // Material config.base is relative to the current page (e.g. "../..")
    try {
      const cfg = document.getElementById("__config");
      if (cfg) {
        const base = JSON.parse(cfg.textContent).base || ".";
        const abs = new URL(base.endsWith("/") ? base : base + "/", location.href);
        return abs.pathname.replace(/\/$/, "");
      }
    } catch (_) {
      /* fall through */
    }
    return "";
  }

  function conceptUrl(slug) {
    return `${siteRoot()}/crosswalks/concepts/${slug}/`;
  }

  function dataUrl(name) {
    // Root-absolute path — immune to trailing-slash / nested-page quirks
    return [`${siteRoot()}/explore/data/${name}`];
  }

  async function fetchFirst(urls) {
    const errors = [];
    for (const url of urls) {
      try {
        const res = await fetch(url);
        if (res.ok) return res.json();
        errors.push(`${url} → HTTP ${res.status}`);
      } catch (err) {
        errors.push(`${url} → ${err && err.message ? err.message : err}`);
      }
    }
    throw new Error("Could not load explore data. " + errors.join("; "));
  }

  const SVG_NS = "http://www.w3.org/2000/svg";
  const SVG_TAGS = new Set(["svg", "g", "line", "circle", "text", "title", "path", "rect"]);

  function el(tag, attrs = {}, children = []) {
    const node = SVG_TAGS.has(tag)
      ? document.createElementNS(SVG_NS, tag)
      : document.createElement(tag);
    Object.entries(attrs).forEach(([k, v]) => {
      if (k === "className") {
        if (SVG_TAGS.has(tag)) node.setAttribute("class", v);
        else node.className = v;
      } else if (k === "text") {
        node.textContent = v;
      } else if (k === "html") {
        node.innerHTML = v;
      } else if (k === "style" && !SVG_TAGS.has(tag)) {
        node.setAttribute("style", v);
      } else {
        node.setAttribute(k, v);
      }
    });
    children.forEach((c) => node.appendChild(typeof c === "string" ? document.createTextNode(c) : c));
    return node;
  }

  function renderCoverageMatrix(root, payload) {
    const table = el("table", { className: "xwk-matrix" });
    const thead = el("thead");
    const headRow = el("tr");
    headRow.appendChild(el("th", { text: "Concept" }));
    payload.source_order.forEach((ont) => headRow.appendChild(el("th", { text: ont, title: ont })));
    thead.appendChild(headRow);
    table.appendChild(thead);

    const tbody = el("tbody");
    payload.coverage_matrix.forEach((row) => {
      const tr = el("tr");
      const link = el("a", { href: conceptUrl(row.slug), text: row.title });
      tr.appendChild(el("th", {}, [link]));
      payload.source_order.forEach((ont) => {
        const n = row.counts[ont] || 0;
        const td = el("td", {
          className: n ? "xwk-hit" : "xwk-miss",
          title: n ? `${ont}: ${n} correspondence(s)` : `${ont}: no correspondence row`,
          text: n ? String(n) : "·",
        });
        if (n) td.style.backgroundColor = SOURCE_COLORS[ont] || "#0f766e";
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    root.replaceChildren(table);

    const legend = el("div", { className: "xwk-legend" });
    payload.source_order.forEach((ont) => {
      const swatch = el("span", { className: "xwk-swatch" });
      swatch.style.background = SOURCE_COLORS[ont];
      legend.appendChild(el("span", { className: "xwk-legend-item" }, [swatch, document.createTextNode(ont)]));
    });
    root.appendChild(legend);
  }

  function renderNetwork(root, payload) {
    const controls = el("div", { className: "xwk-controls" });
    const select = el("select", { id: "xwk-concept-select", "aria-label": "Choose concept" });
    payload.concepts.forEach((c) => {
      select.appendChild(el("option", { value: c.slug, text: `${c.title} (${c.mapping_count} mappings)` }));
    });
    controls.appendChild(el("label", { text: "Concept " }));
    controls.appendChild(select);

    const meta = el("p", { className: "xwk-meta" });
    const svgWrap = el("div", { className: "xwk-svg-wrap" });
    const tip = el("div", { className: "xwk-tip" });
    tip.hidden = true;

    root.replaceChildren(controls, meta, svgWrap);

    function draw(slug) {
      const concept = payload.concepts.find((c) => c.slug === slug);
      if (!concept) return;
      meta.replaceChildren(
        el("a", { href: conceptUrl(concept.slug), text: concept.title }),
        document.createTextNode(
          ` — ${concept.correspondence_count} correspondences, ${concept.mapping_count} mapping assertions across ${concept.ontologies.length} sources.`
        )
      );

      const width = Math.max(svgWrap.clientWidth || 720, 640);
      const height = 520;
      svgWrap.replaceChildren();
      tip.hidden = true;
      const svg = el("svg", {
        viewBox: `0 0 ${width} ${height}`,
        width: "100%",
        height: String(height),
        class: "xwk-network",
        role: "img",
        "aria-label": `Mapping network for ${concept.title}`,
      });
      svgWrap.appendChild(svg);
      svgWrap.appendChild(tip);

      // Build nodes from mapping endpoints + correspondence terms
      const nodes = new Map();
      function ensureNode(id, ontology, label) {
        if (!id) return null;
        if (!nodes.has(id)) {
          nodes.set(id, {
            id,
            ontology: ontology || ontology_from_id(id),
            label: label || id,
            x: width / 2 + (Math.random() - 0.5) * 120,
            y: height / 2 + (Math.random() - 0.5) * 120,
            vx: 0,
            vy: 0,
          });
        }
        return nodes.get(id);
      }

      function ontology_from_id(id) {
        const p = id.split(":")[0];
        return p === "TUPPER" ? "TUpper" : p;
      }

      const links = [];
      concept.mappings.forEach((m) => {
        const a = ensureNode(m.subject, m.subject_ontology, m.subject);
        const b = ensureNode(m.object, m.object_ontology, m.object);
        if (a && b) {
          links.push({
            source: a,
            target: b,
            relation: m.relation || "unknown",
            confidence: m.confidence || "",
          });
        }
      });

      // If no mappings, show correspondence terms as a ring
      if (!links.length) {
        concept.correspondences.forEach((c, i) => {
          const id = `${c.ontology}:${c.term || i}`;
          ensureNode(id, c.ontology, `${c.ontology}: ${c.term}`);
        });
      }

      const nodeList = Array.from(nodes.values());
      if (!nodeList.length) {
        svg.appendChild(
          el("text", {
            x: String(width / 2),
            y: String(height / 2),
            "text-anchor": "middle",
            fill: "currentColor",
            text: "No mapping or correspondence nodes for this concept.",
          })
        );
        return;
      }

      // Seed positions on a circle by ontology
      const byOnt = {};
      nodeList.forEach((n) => {
        const o = n.ontology || "Other";
        (byOnt[o] ||= []).push(n);
      });
      const ontKeys = Object.keys(byOnt);
      ontKeys.forEach((ont, oi) => {
        const angle0 = (oi / ontKeys.length) * Math.PI * 2;
        byOnt[ont].forEach((n, ni) => {
          const r = 140 + (ni % 3) * 28;
          const a = angle0 + (ni * 0.35) / Math.max(byOnt[ont].length, 1);
          n.x = width / 2 + Math.cos(a) * r;
          n.y = height / 2 + Math.sin(a) * r;
        });
      });

      const gLinks = el("g", { class: "links" });
      const gNodes = el("g", { class: "nodes" });
      svg.appendChild(gLinks);
      svg.appendChild(gNodes);

      const linkEls = links.map((l) => {
        const line = el("line", {
          stroke: RELATION_COLORS[l.relation] || RELATION_COLORS.unknown,
          "stroke-width": "2",
          "stroke-opacity": "0.75",
        });
        line.addEventListener("mouseenter", (ev) => showTip(ev, `${l.source.label} —[${l.relation}]→ ${l.target.label}`));
        line.addEventListener("mouseleave", hideTip);
        gLinks.appendChild(line);
        return { line, l };
      });

      const nodeEls = nodeList.map((n) => {
        const g = el("g", { class: "node", style: "cursor:grab" });
        const circle = el("circle", {
          r: "10",
          fill: SOURCE_COLORS[n.ontology] || "#475569",
          stroke: "#0f172a",
          "stroke-width": "1",
        });
        const label = el("text", {
          "font-size": "11",
          fill: "currentColor",
          dy: "20",
          "text-anchor": "middle",
          text: shorten(n.label, 28),
        });
        g.appendChild(circle);
        g.appendChild(label);
        g.addEventListener("mouseenter", (ev) => showTip(ev, `${n.label}`));
        g.addEventListener("mouseleave", hideTip);
        enableDrag(g, n);
        gNodes.appendChild(g);
        return { g, n };
      });

      function showTip(ev, text) {
        tip.hidden = false;
        tip.textContent = text;
        const rect = svgWrap.getBoundingClientRect();
        tip.style.left = `${ev.clientX - rect.left + 12}px`;
        tip.style.top = `${ev.clientY - rect.top + 12}px`;
      }
      function hideTip() {
        tip.hidden = true;
      }

      function enableDrag(g, n) {
        let dragging = false;
        g.addEventListener("pointerdown", (ev) => {
          dragging = true;
          g.setPointerCapture(ev.pointerId);
        });
        g.addEventListener("pointermove", (ev) => {
          if (!dragging) return;
          const rect = svg.getBoundingClientRect();
          n.x = ((ev.clientX - rect.left) / rect.width) * width;
          n.y = ((ev.clientY - rect.top) / rect.height) * height;
          n.vx = 0;
          n.vy = 0;
        });
        g.addEventListener("pointerup", () => {
          dragging = false;
        });
      }

      function tick() {
        // Simple force simulation
        for (let i = 0; i < nodeList.length; i++) {
          for (let j = i + 1; j < nodeList.length; j++) {
            const a = nodeList[i];
            const b = nodeList[j];
            let dx = a.x - b.x;
            let dy = a.y - b.y;
            let dist = Math.hypot(dx, dy) || 0.01;
            const force = 800 / (dist * dist);
            dx = (dx / dist) * force;
            dy = (dy / dist) * force;
            a.vx += dx;
            a.vy += dy;
            b.vx -= dx;
            b.vy -= dy;
          }
        }
        links.forEach((l) => {
          const dx = l.target.x - l.source.x;
          const dy = l.target.y - l.source.y;
          const dist = Math.hypot(dx, dy) || 0.01;
          const desired = 110;
          const force = (dist - desired) * 0.02;
          const fx = (dx / dist) * force;
          const fy = (dy / dist) * force;
          l.source.vx += fx;
          l.source.vy += fy;
          l.target.vx -= fx;
          l.target.vy -= fy;
        });
        nodeList.forEach((n) => {
          // mild center gravity
          n.vx += (width / 2 - n.x) * 0.002;
          n.vy += (height / 2 - n.y) * 0.002;
          n.vx *= 0.85;
          n.vy *= 0.85;
          n.x = Math.min(width - 24, Math.max(24, n.x + n.vx));
          n.y = Math.min(height - 28, Math.max(24, n.y + n.vy));
        });

        linkEls.forEach(({ line, l }) => {
          line.setAttribute("x1", l.source.x);
          line.setAttribute("y1", l.source.y);
          line.setAttribute("x2", l.target.x);
          line.setAttribute("y2", l.target.y);
        });
        nodeEls.forEach(({ g, n }) => {
          g.setAttribute("transform", `translate(${n.x},${n.y})`);
        });
        requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    }

    function shorten(s, n) {
      return s.length > n ? s.slice(0, n - 1) + "…" : s;
    }

    select.addEventListener("change", () => draw(select.value));
    const preferred = payload.concepts.find((c) => c.slug === "object") || payload.concepts[0];
    if (preferred) {
      select.value = preferred.slug;
      draw(preferred.slug);
    }
  }

  function renderStats(root, payload) {
    const totalMappings = payload.concepts.reduce((s, c) => s + c.mapping_count, 0);
    const totalCorr = payload.concepts.reduce((s, c) => s + c.correspondence_count, 0);
    root.replaceChildren(
      el("div", { className: "xwk-stats" }, [
        stat("Concepts", payload.concept_count),
        stat("Correspondences", totalCorr),
        stat("Mapping assertions", totalMappings),
        stat("Source ontologies", payload.source_order.length),
      ])
    );
  }

  function stat(label, value) {
    return el("div", { className: "xwk-stat" }, [
      el("div", { className: "xwk-stat-value", text: String(value) }),
      el("div", { className: "xwk-stat-label", text: label }),
    ]);
  }

  const CLOUD_COLORS = ["#0f766e", "#0369a1", "#334155", "#b45309", "#047857", "#1d4ed8", "#be123c", "#0e7490"];

  function conceptWeight(c, mode) {
    if (mode === "mappings") return Math.max(1, c.mapping_count || 0);
    if (mode === "correspondences") return Math.max(1, c.correspondence_count || 0);
    return Math.max(1, (c.mapping_count || 0) + (c.correspondence_count || 0));
  }

  function renderWordCloud(root, payload) {
    const controls = el("div", { className: "xwk-controls" });
    const select = el("select", { id: "xwk-cloud-weight", "aria-label": "Word size by" });
    [
      ["mappings", "Size by mapping assertions"],
      ["correspondences", "Size by correspondence rows"],
      ["combined", "Size by mappings + correspondences"],
    ].forEach(([value, text]) => select.appendChild(el("option", { value, text })));
    select.value = "mappings";
    controls.appendChild(el("label", { text: "Weight " }));
    controls.appendChild(select);

    const meta = el("p", { className: "xwk-meta" });
    const svgWrap = el("div", { className: "xwk-svg-wrap xwk-cloud-wrap" });
    const tip = el("div", { className: "xwk-tip" });
    tip.hidden = true;
    root.replaceChildren(controls, meta, svgWrap);

    const measureCtx = document.createElement("canvas").getContext("2d");
    const pageFont = getComputedStyle(document.body).fontFamily || "sans-serif";

    function measure(text, fontSize) {
      measureCtx.font = `600 ${fontSize}px ${pageFont}`;
      const w = measureCtx.measureText(text).width;
      // Slightly tall boxes so descenders / visual weight do not collide
      return { w: w + 6, h: fontSize * 1.35 };
    }

    function overlaps(a, b, pad) {
      return !(
        a.x + a.w / 2 + pad < b.x - b.w / 2 ||
        a.x - a.w / 2 - pad > b.x + b.w / 2 ||
        a.y + a.h / 2 + pad < b.y - b.h / 2 ||
        a.y - a.h / 2 - pad > b.y + b.h / 2
      );
    }

    function inBounds(item, width, height, margin) {
      return (
        item.x - item.w / 2 >= margin &&
        item.x + item.w / 2 <= width - margin &&
        item.y - item.h / 2 >= margin &&
        item.y + item.h / 2 <= height - margin
      );
    }

    function tryPlace(items, width, height, pad) {
      const cx = width / 2;
      const cy = height / 2;
      const placed = [];
      for (let idx = 0; idx < items.length; idx++) {
        const item = items[idx];
        let found = false;
        const maxSteps = 12000;
        for (let step = 0; step < maxSteps; step++) {
          // Archimedean spiral — fine steps, mild vertical squash
          const t = step * 0.12;
          const r = step === 0 && idx === 0 ? 0 : 6 + t * 2.1;
          item.x = cx + Math.cos(t) * r;
          item.y = cy + Math.sin(t) * r * 0.78;
          if (inBounds(item, width, height, 10) && !placed.some((p) => overlaps(item, p, pad))) {
            found = true;
            break;
          }
        }
        if (!found) return false;
        placed.push(item);
      }
      return true;
    }

    function separate(items, width, height, rounds) {
      for (let round = 0; round < rounds; round++) {
        for (let i = 0; i < items.length; i++) {
          for (let j = i + 1; j < items.length; j++) {
            const a = items[i];
            const b = items[j];
            const pad = 6;
            if (!overlaps(a, b, pad)) continue;
            let dx = a.x - b.x;
            let dy = a.y - b.y;
            let dist = Math.hypot(dx, dy) || 0.01;
            const minDist = (a.w + b.w) / 4 + (a.h + b.h) / 4 + pad;
            if (dist >= minDist) continue;
            const push = ((minDist - dist) / dist) * 0.5;
            dx *= push;
            dy *= push;
            a.x += dx;
            a.y += dy;
            b.x -= dx;
            b.y -= dy;
          }
        }
        items.forEach((item) => {
          item.x = Math.min(width - 10 - item.w / 2, Math.max(10 + item.w / 2, item.x));
          item.y = Math.min(height - 10 - item.h / 2, Math.max(10 + item.h / 2, item.y));
        });
      }
    }

    function buildItems(mode, fontScale) {
      const weights = payload.concepts.map((c) => conceptWeight(c, mode));
      const minW = Math.min(...weights);
      const maxW = Math.max(...weights);
      const span = Math.max(maxW - minW, 1);
      return payload.concepts
        .map((c, i) => {
          const weight = conceptWeight(c, mode);
          const t = (weight - minW) / span;
          const fontSize = Math.max(11, Math.round((12 + t * 22) * fontScale));
          const short = c.title.length > 24 ? c.title.slice(0, 23) + "…" : c.title;
          const box = measure(short, fontSize);
          return {
            ...c,
            weight,
            fontSize,
            short,
            w: box.w,
            h: box.h,
            color: CLOUD_COLORS[i % CLOUD_COLORS.length],
          };
        })
        .sort((a, b) => b.weight - a.weight || a.title.localeCompare(b.title));
    }

    function layout(mode) {
      const width = Math.max(svgWrap.clientWidth || 860, 720);
      let height = Math.max(560, Math.round(width * 0.72));
      let fontScale = 1;
      let items = null;

      for (let attempt = 0; attempt < 10; attempt++) {
        items = buildItems(mode, fontScale);
        if (tryPlace(items, width, height, 7)) {
          separate(items, width, height, 40);
          // If separation reintroduced hard overlaps, accept; spiral already non-overlapping
          return { items, width, height };
        }
        // Grow canvas, then shrink fonts if still cramped
        if (attempt < 5) height += 80;
        else fontScale *= 0.9;
      }
      // Last resort: still place with oversized canvas
      height += 200;
      items = buildItems(mode, fontScale * 0.85);
      tryPlace(items, width, height, 5);
      separate(items, width, height, 60);
      return { items, width, height };
    }

    function draw(mode) {
      const { items, width, height } = layout(mode);

      meta.textContent = `${payload.concepts.length} reviewed concepts · sized by ${
        mode === "mappings" ? "mapping assertions" : mode === "correspondences" ? "correspondence rows" : "mappings + correspondences"
      } · click a label to open its crosswalk`;
      svgWrap.replaceChildren();
      tip.hidden = true;

      const svg = el("svg", {
        viewBox: `0 0 ${width} ${height}`,
        width: "100%",
        height: String(height),
        class: "xwk-network xwk-cloud",
        role: "img",
        "aria-label": "Word cloud of reviewed XwkOnt concepts",
      });
      svgWrap.appendChild(svg);
      svgWrap.appendChild(tip);

      items.forEach((item) => {
        const g = el("g", {
          class: "xwk-cloud-word",
          transform: `translate(${item.x},${item.y})`,
          style: "cursor:pointer",
        });
        const text = el("text", {
          "text-anchor": "middle",
          "dominant-baseline": "middle",
          "font-size": String(item.fontSize),
          "font-weight": "600",
          fill: item.color,
          text: item.short,
        });
        g.appendChild(text);
        g.addEventListener("mouseenter", (ev) => {
          tip.hidden = false;
          tip.textContent = `${item.title} — ${item.mapping_count} mappings, ${item.correspondence_count} correspondences`;
          const rect = svgWrap.getBoundingClientRect();
          tip.style.left = `${ev.clientX - rect.left + 12}px`;
          tip.style.top = `${ev.clientY - rect.top + 12}px`;
        });
        g.addEventListener("mousemove", (ev) => {
          const rect = svgWrap.getBoundingClientRect();
          tip.style.left = `${ev.clientX - rect.left + 12}px`;
          tip.style.top = `${ev.clientY - rect.top + 12}px`;
        });
        g.addEventListener("mouseleave", () => {
          tip.hidden = true;
        });
        g.addEventListener("click", () => {
          location.href = conceptUrl(item.slug);
        });
        svg.appendChild(g);
      });
    }

    select.addEventListener("change", () => draw(select.value));
    let resizeTimer = 0;
    window.addEventListener("resize", () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => draw(select.value), 150);
    });
    draw(select.value);
  }

  function prettyLabel(id) {
    return id
      .replace(/([a-z])([A-Z])/g, "$1 $2")
      .replace(/Stratum$/, " / Stratum")
      .replace(/Sequence$/, " / Sequence")
      .replace(/Artifact$/, " Artifact")
      .replace(/Object$/, (m, off, s) => (s.startsWith("NonPhysical") ? " Object" : m));
  }

  function renderCoreHierarchy(root, hierarchy) {
    const controls = el("div", { className: "xwk-controls" });
    const relToggle = el("input", { type: "checkbox", id: "xwk-core-rels" });
    relToggle.checked = true;
    const resetBtn = el("button", { type: "button", className: "xwk-btn", text: "Reset layout" });
    controls.appendChild(el("label", {}, [relToggle, document.createTextNode(" Show relation edges")]));
    controls.appendChild(resetBtn);

    const meta = el("p", { className: "xwk-meta", text: `${hierarchy.classes.length} classes · drag nodes · click to highlight ancestry/descendants` });
    const svgWrap = el("div", { className: "xwk-svg-wrap xwk-core-wrap" });
    const tip = el("div", { className: "xwk-tip" });
    tip.hidden = true;
    root.replaceChildren(controls, meta, svgWrap);

    const children = {};
    const parents = {};
    hierarchy.classes.forEach((c) => {
      children[c] = [];
    });
    hierarchy.inheritance.forEach(({ parent, child }) => {
      (children[parent] ||= []).push(child);
      parents[child] = parent;
    });

    const levels = {};
    function depth(id) {
      if (levels[id] != null) return levels[id];
      levels[id] = parents[id] ? depth(parents[id]) + 1 : 0;
      return levels[id];
    }
    hierarchy.classes.forEach(depth);
    const maxDepth = Math.max(...Object.values(levels), 0);
    const byLevel = {};
    hierarchy.classes.forEach((c) => {
      (byLevel[levels[c]] ||= []).push(c);
    });
    Object.values(byLevel).forEach((arr) => arr.sort());

    let selected = null;
    let showRels = true;
    let raf = 0;

    function layoutSeed(width, height) {
      const nodes = {};
      hierarchy.classes.forEach((id) => {
        const level = levels[id];
        const row = byLevel[level];
        const idx = row.indexOf(id);
        const x = ((idx + 1) / (row.length + 1)) * (width - 80) + 40;
        const y = ((level + 0.55) / (maxDepth + 1.2)) * (height - 60) + 30;
        nodes[id] = { id, x, y, vx: 0, vy: 0, level };
      });
      return nodes;
    }

    function neighborhood(id) {
      const set = new Set([id]);
      let p = parents[id];
      while (p) {
        set.add(p);
        p = parents[p];
      }
      const stack = [...(children[id] || [])];
      while (stack.length) {
        const c = stack.pop();
        if (set.has(c)) continue;
        set.add(c);
        (children[c] || []).forEach((x) => stack.push(x));
      }
      return set;
    }

    function draw() {
      if (raf) cancelAnimationFrame(raf);
      const width = Math.max(svgWrap.clientWidth || 860, 720);
      const height = Math.max(420 + maxDepth * 70, 560);
      const nodes = layoutSeed(width, height);
      svgWrap.replaceChildren();
      tip.hidden = true;

      const svg = el("svg", {
        viewBox: `0 0 ${width} ${height}`,
        width: "100%",
        height: String(height),
        class: "xwk-network",
        role: "img",
        "aria-label": "Interactive XwkOnt core class hierarchy",
      });
      const gRels = el("g", { class: "rels" });
      const gInh = el("g", { class: "inh" });
      const gNodes = el("g", { class: "nodes" });
      svg.appendChild(gRels);
      svg.appendChild(gInh);
      svg.appendChild(gNodes);
      svgWrap.appendChild(svg);
      svgWrap.appendChild(tip);

      const inhLines = hierarchy.inheritance.map((e) => {
        const line = el("line", {
          "stroke-width": "2",
          "stroke-opacity": "0.7",
          stroke: "#0f766e",
        });
        gInh.appendChild(line);
        return { line, e };
      });

      const relLines = (hierarchy.relations || []).map((e) => {
        const line = el("line", {
          "stroke-width": "1.5",
          "stroke-opacity": "0.55",
          stroke: "#0369a1",
          "stroke-dasharray": "5 4",
        });
        line.addEventListener("mouseenter", (ev) =>
          showTip(ev, `${e.source} —[${e.label || "related"}]→ ${e.target}`)
        );
        line.addEventListener("mouseleave", hideTip);
        gRels.appendChild(line);
        return { line, e };
      });

      const nodeEls = hierarchy.classes.map((id) => {
        const n = nodes[id];
        const g = el("g", { class: "node", style: "cursor:grab" });
        const labelText = prettyLabel(id);
        const tw = Math.min(Math.max(labelText.length * 6.2 + 18, 64), 150);
        const rect = el("rect", {
          x: String(-tw / 2),
          y: "-14",
          width: String(tw),
          height: "28",
          rx: "8",
          fill: id === "Entity" ? "#0f766e" : "#334155",
          stroke: "#0f172a",
          "stroke-width": "1",
        });
        const text = el("text", {
          "text-anchor": "middle",
          dy: "4",
          "font-size": "11",
          fill: "#f8fafc",
          text: labelText.length > 22 ? labelText.slice(0, 21) + "…" : labelText,
        });
        g.appendChild(rect);
        g.appendChild(text);
        g.addEventListener("mouseenter", (ev) => {
          const parent = parents[id] ? ` · parent ${prettyLabel(parents[id])}` : " · root";
          const kids = (children[id] || []).length;
          showTip(ev, `${prettyLabel(id)}${parent} · ${kids} child class(es)`);
        });
        g.addEventListener("mouseleave", hideTip);
        g.addEventListener("click", (ev) => {
          ev.stopPropagation();
          selected = selected === id ? null : id;
          paint();
        });
        enableDrag(g, n);
        gNodes.appendChild(g);
        return { g, rect, n, id };
      });

      function showTip(ev, text) {
        tip.hidden = false;
        tip.textContent = text;
        const rect = svgWrap.getBoundingClientRect();
        tip.style.left = `${ev.clientX - rect.left + 12}px`;
        tip.style.top = `${ev.clientY - rect.top + 12}px`;
      }
      function hideTip() {
        tip.hidden = true;
      }

      function enableDrag(g, n) {
        let dragging = false;
        g.addEventListener("pointerdown", (ev) => {
          dragging = true;
          g.setPointerCapture(ev.pointerId);
          ev.preventDefault();
        });
        g.addEventListener("pointermove", (ev) => {
          if (!dragging) return;
          const rect = svg.getBoundingClientRect();
          n.x = ((ev.clientX - rect.left) / rect.width) * width;
          n.y = ((ev.clientY - rect.top) / rect.height) * height;
          n.vx = 0;
          n.vy = 0;
          paint();
        });
        g.addEventListener("pointerup", () => {
          dragging = false;
        });
      }

      function paint() {
        const focus = selected ? neighborhood(selected) : null;
        inhLines.forEach(({ line, e }) => {
          const a = nodes[e.parent];
          const b = nodes[e.child];
          line.setAttribute("x1", a.x);
          line.setAttribute("y1", a.y);
          line.setAttribute("x2", b.x);
          line.setAttribute("y2", b.y);
          const on = !focus || (focus.has(e.parent) && focus.has(e.child));
          line.setAttribute("stroke-opacity", on ? "0.85" : "0.12");
        });
        relLines.forEach(({ line, e }) => {
          line.style.display = showRels ? "" : "none";
          const a = nodes[e.source];
          const b = nodes[e.target];
          // self-loops: small offset arc substitute via short stub
          if (e.source === e.target) {
            line.setAttribute("x1", a.x - 18);
            line.setAttribute("y1", a.y - 18);
            line.setAttribute("x2", a.x + 18);
            line.setAttribute("y2", a.y - 18);
          } else {
            line.setAttribute("x1", a.x);
            line.setAttribute("y1", a.y);
            line.setAttribute("x2", b.x);
            line.setAttribute("y2", b.y);
          }
          const on = !focus || focus.has(e.source) || focus.has(e.target);
          line.setAttribute("stroke-opacity", on ? "0.6" : "0.08");
        });
        nodeEls.forEach(({ g, rect, n, id }) => {
          g.setAttribute("transform", `translate(${n.x},${n.y})`);
          const on = !focus || focus.has(id);
          rect.setAttribute("opacity", on ? "1" : "0.22");
          if (selected === id) {
            rect.setAttribute("stroke", "#5eead4");
            rect.setAttribute("stroke-width", "2.5");
          } else {
            rect.setAttribute("stroke", "#0f172a");
            rect.setAttribute("stroke-width", "1");
          }
        });
      }

      // light force to reduce overlap while preserving levels
      function tick() {
        const list = Object.values(nodes);
        for (let i = 0; i < list.length; i++) {
          for (let j = i + 1; j < list.length; j++) {
            const a = list[i];
            const b = list[j];
            let dx = a.x - b.x;
            let dy = a.y - b.y;
            let dist = Math.hypot(dx, dy) || 0.01;
            if (dist < 90) {
              const f = ((90 - dist) / dist) * 0.08;
              a.vx += dx * f;
              a.vy += dy * f;
              b.vx -= dx * f;
              b.vy -= dy * f;
            }
          }
        }
        list.forEach((n) => {
          const targetY = ((n.level + 0.55) / (maxDepth + 1.2)) * (height - 60) + 30;
          n.vy += (targetY - n.y) * 0.04;
          n.vx *= 0.8;
          n.vy *= 0.8;
          n.x = Math.min(width - 40, Math.max(40, n.x + n.vx));
          n.y = Math.min(height - 30, Math.max(24, n.y + n.vy));
        });
        paint();
        raf = requestAnimationFrame(tick);
      }
      raf = requestAnimationFrame(tick);
      paint();
    }

    relToggle.addEventListener("change", () => {
      showRels = relToggle.checked;
      // repaint relation visibility without full relayout
      draw();
    });
    resetBtn.addEventListener("click", () => {
      selected = null;
      draw();
    });
    let resizeTimer = 0;
    window.addEventListener("resize", () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(draw, 150);
    });
    draw();
  }

  async function boot() {
    const matrixRoot = document.getElementById("xwk-coverage-matrix");
    const networkRoot = document.getElementById("xwk-mapping-network");
    const statsRoot = document.getElementById("xwk-explore-stats");
    const coreRoot = document.getElementById("xwk-core-hierarchy");
    const cloudRoot = document.getElementById("xwk-concept-cloud");
    if (!matrixRoot && !networkRoot && !statsRoot && !coreRoot && !cloudRoot) return;

    try {
      if (statsRoot || matrixRoot || networkRoot || cloudRoot) {
        const payload = await fetchFirst(dataUrl("crosswalks.json"));
        if (statsRoot) renderStats(statsRoot, payload);
        if (matrixRoot) renderCoverageMatrix(matrixRoot, payload);
        if (networkRoot) renderNetwork(networkRoot, payload);
        if (cloudRoot) renderWordCloud(cloudRoot, payload);
      }
      if (coreRoot) {
        const hierarchy = await fetchFirst(dataUrl("core-hierarchy.json"));
        renderCoreHierarchy(coreRoot, hierarchy);
      }
    } catch (err) {
      const msg = el("p", { className: "xwk-error", text: String(err.message || err) });
      [matrixRoot, networkRoot, statsRoot, coreRoot, cloudRoot].forEach((r) => r && r.replaceChildren(msg.cloneNode(true)));
    }
  }

  function start() {
    boot().catch((err) => {
      const msg = document.createElement("p");
      msg.className = "xwk-error";
      msg.textContent = String(err && err.message ? err.message : err);
      ["xwk-coverage-matrix", "xwk-mapping-network", "xwk-explore-stats", "xwk-core-hierarchy", "xwk-concept-cloud"].forEach((id) => {
        const r = document.getElementById(id);
        if (r) r.replaceChildren(msg.cloneNode(true));
      });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
