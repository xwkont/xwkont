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
    return match ? match[1] : "";
  }

  function conceptUrl(slug) {
    return `${siteRoot()}/crosswalks/concepts/${slug}/`;
  }

  function dataUrl(name) {
    const path = location.pathname.replace(/index\.html$/, "");
    if (/\/explore\/?$/.test(path)) {
      return [`data/${name}`, `./data/${name}`];
    }
    if (/\/explore\//.test(path)) {
      return [`../data/${name}`, `./data/${name}`, `data/${name}`];
    }
    return [
      `explore/data/${name}`,
      `../explore/data/${name}`,
      `./data/${name}`,
      `data/${name}`,
    ];
  }

  async function fetchFirst(urls) {
    for (const url of urls) {
      try {
        const res = await fetch(url);
        if (res.ok) return res.json();
      } catch (_) {
        /* try next */
      }
    }
    throw new Error("Could not load explore data: " + urls.join(", "));
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

  async function boot() {
    const matrixRoot = document.getElementById("xwk-coverage-matrix");
    const networkRoot = document.getElementById("xwk-mapping-network");
    const statsRoot = document.getElementById("xwk-explore-stats");
    if (!matrixRoot && !networkRoot && !statsRoot) return;

    try {
      const payload = await fetchFirst(dataUrl("crosswalks.json"));
      if (statsRoot) renderStats(statsRoot, payload);
      if (matrixRoot) renderCoverageMatrix(matrixRoot, payload);
      if (networkRoot) renderNetwork(networkRoot, payload);
    } catch (err) {
      const msg = el("p", { className: "xwk-error", text: String(err.message || err) });
      [matrixRoot, networkRoot, statsRoot].forEach((r) => r && r.replaceChildren(msg.cloneNode(true)));
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
