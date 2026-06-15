from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .analyzer import run_analysis
from .config import load_config, load_prompt_templates
from .ollama_client import check_ollama
from .pdf_processor import process_papers, load_processed_papers


app = FastAPI(title="LLM2 Revision Cientifica", version="1.0.0")


class AnalyzeRequest(BaseModel):
    model_id: str = "all"
    prompt_id: str = "all"
    activity_id: str = "all"
    mock: bool = False


@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse(HTML)


@app.get("/api/status")
def status():
    config = load_config()
    processed = load_processed_papers(config)
    prompts = load_prompt_templates()
    ok_papers = [paper for paper in processed.get("papers", []) if paper.get("status") == "ok"]
    ollama_status = check_ollama(config["ollama"]["base_url"])
    return {
        "project": config["project"],
        "models": config["models"],
        "activities": config["activities"],
        "prompts": [{"id": item["id"], "name": item["name"]} for item in prompts],
        "papers": processed["papers"],
        "paper_count": len(ok_papers),
        "required_papers": config["project"].get("required_papers", 4),
        "ollama": ollama_status,
        "fallback_to_demo": bool(config["ollama"].get("fallback_to_demo", False)),
    }


@app.post("/api/process-pdfs")
def process_pdfs():
    config = load_config()
    return process_papers(config)


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    config = load_config()
    try:
        return run_analysis(
            config,
            model_id=req.model_id,
            prompt_id=req.prompt_id,
            activity_id=req.activity_id,
            mock=req.mock,
        )
    except KeyError as exc:
        raise HTTPException(status_code=400, detail=f"Seleccion no valida: {exc}") from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


HTML = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LLM2 - Revision cientifica local</title>
  <style>
    :root {
      --bg: #f5f7fb;
      --panel: #ffffff;
      --ink: #172033;
      --muted: #64748b;
      --line: #d9e1ec;
      --accent: #285d8f;
      --good: #047857;
      --warn: #b45309;
      --bad: #b91c1c;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    body { margin: 0; background: var(--bg); color: var(--ink); }
    header { background: var(--panel); border-bottom: 1px solid var(--line); padding: 18px 24px; }
    main { width: min(1220px, calc(100% - 28px)); margin: 22px auto 48px; }
    h1 { margin: 0; font-size: 24px; }
    h2 { font-size: 18px; margin: 0 0 12px; }
    p { line-height: 1.5; }
    .subtitle { color: var(--muted); margin: 6px 0 0; }
    .panel, .toolbar {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
      box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05);
      margin-bottom: 16px;
    }
    .toolbar {
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 12px;
      align-items: end;
    }
    label { display: grid; gap: 6px; color: var(--muted); font-size: 13px; font-weight: 700; }
    select, button {
      min-height: 40px;
      border-radius: 6px;
      font: inherit;
    }
    select { border: 1px solid var(--line); padding: 0 10px; background: white; color: var(--ink); }
    button { border: 0; padding: 0 14px; background: var(--accent); color: white; font-weight: 800; cursor: pointer; }
    button.secondary { background: #475569; }
    button:disabled { opacity: .55; cursor: wait; }
    .check { display: flex; align-items: center; gap: 8px; min-height: 40px; }
    .check input { width: 18px; height: 18px; }
    .grid { display: grid; grid-template-columns: 1fr; gap: 16px; }
    .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }
    .card { border: 1px solid var(--line); border-radius: 8px; padding: 14px; background: #fbfdff; }
    .card b { display: block; font-size: 20px; margin-top: 5px; }
    .muted { color: var(--muted); }
    .status { color: var(--muted); min-height: 24px; margin: 10px 0 16px; }
    .table-wrap { overflow-x: auto; border: 1px solid var(--line); border-radius: 8px; }
    table { border-collapse: collapse; width: 100%; min-width: 900px; background: white; }
    th, td { padding: 10px 12px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; font-size: 14px; }
    th { background: #f8fafc; color: #475569; text-transform: uppercase; font-size: 12px; letter-spacing: .03em; }
    tr:last-child td { border-bottom: 0; }
    .pill { display: inline-block; padding: 3px 8px; border-radius: 999px; font-size: 12px; font-weight: 800; background: #e2e8f0; color: #334155; }
    .pill.good { background: #dcfce7; color: var(--good); }
    .pill.warn { background: #fef3c7; color: var(--warn); }
    .pill.bad { background: #fee2e2; color: var(--bad); }
    details summary { cursor: pointer; color: var(--accent); font-weight: 700; }
    pre { white-space: pre-wrap; max-height: 360px; overflow: auto; background: #f8fafc; border: 1px solid var(--line); border-radius: 6px; padding: 10px; }
    code { background: #eef2ff; padding: 2px 5px; border-radius: 4px; }
    @media (max-width: 780px) {
      header { padding: 14px 16px; }
      main { width: min(100% - 20px, 1220px); margin-top: 14px; }
      .toolbar { grid-template-columns: 1fr; }
      h1 { font-size: 20px; }
      table { min-width: 780px; }
    }
  </style>
</head>
<body>
  <header>
    <h1>LLM2 - Revision cientifica con modelos locales</h1>
    <p class="subtitle">Tema: lenguaje natural, redes complejas y analisis topologico de datos.</p>
  </header>
  <main>
    <section class="panel">
      <h2>Proyecto</h2>
      <div id="project"></div>
      <div id="warnings"></div>
    </section>

    <section class="toolbar">
      <label>Modelo
        <select id="model"></select>
      </label>
      <label>Prompt
        <select id="prompt"></select>
      </label>
      <label>Actividad
        <select id="activity"></select>
      </label>
      <label class="check">
        <input id="mock" type="checkbox">
        Simular sin Ollama
      </label>
      <button id="runBtn">Ejecutar analisis</button>
      <button class="secondary" id="processBtn">Procesar PDFs</button>
    </section>

    <p class="status" id="status">Cargando configuracion...</p>

    <section class="grid">
      <div class="panel">
        <h2>Articulos</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th>ID</th><th>Titulo</th><th>Fuente</th><th>Estado</th><th>Palabras</th><th>Ruta</th></tr></thead>
            <tbody id="papers"></tbody>
          </table>
        </div>
      </div>

      <div class="panel">
        <h2>Resumen de corrida</h2>
        <div id="summary" class="cards"></div>
      </div>

      <div class="panel">
        <h2>Resultados</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Modelo</th><th>Prompt</th><th>Actividad</th><th>Estado</th><th>Tiempo</th><th>Respuesta</th></tr></thead>
            <tbody id="results"><tr><td colspan="6" class="muted">Sin resultados todavia.</td></tr></tbody>
          </table>
        </div>
      </div>
    </section>
  </main>

  <script>
    const els = {
      project: document.getElementById("project"),
      warnings: document.getElementById("warnings"),
      status: document.getElementById("status"),
      model: document.getElementById("model"),
      prompt: document.getElementById("prompt"),
      activity: document.getElementById("activity"),
      mock: document.getElementById("mock"),
      papers: document.getElementById("papers"),
      summary: document.getElementById("summary"),
      results: document.getElementById("results"),
      runBtn: document.getElementById("runBtn"),
      processBtn: document.getElementById("processBtn"),
    };

    function option(value, label) {
      return `<option value="${value}">${label}</option>`;
    }

    function pill(status) {
      const cls = status === "ok" ? "good" : (status === "missing" || status === "fallback" ? "warn" : "bad");
      return `<span class="pill ${cls}">${status}</span>`;
    }

    function renderStatus(data) {
      els.project.innerHTML = `
        <p><b>${data.project.topic}</b></p>
        <p>${data.project.problem_statement}</p>
      `;
      const missing = data.required_papers - data.paper_count;
      els.warnings.innerHTML = missing > 0
        ? `<p><span class="pill warn">Faltan ${missing} articulo(s)</span> La tarea pide ${data.required_papers}; actualmente hay ${data.paper_count} procesado(s).</p>`
        : `<p><span class="pill good">Articulos completos</span> Hay ${data.paper_count}/${data.required_papers} articulos.</p>`;
      els.warnings.innerHTML += data.ollama.available
        ? `<p><span class="pill good">Ollama activo</span> Modelos detectados: ${data.ollama.models.join(", ") || "ninguno"}.</p>`
        : `<p><span class="pill warn">Ollama no disponible</span> ${data.ollama.error} ${data.fallback_to_demo ? "La app usara modo fallback/demo automaticamente." : ""}</p>`;

      els.model.innerHTML = option("all", "Todos") + data.models.map(m => option(m.id, m.label)).join("");
      els.prompt.innerHTML = option("all", "Todos") + data.prompts.map(p => option(p.id, p.name)).join("");
      els.activity.innerHTML = option("all", "Todas") + data.activities.map(a => option(a.id, a.name)).join("");

      els.papers.innerHTML = data.papers.map(p => `
        <tr>
          <td><code>${p.id}</code></td>
          <td>${p.title}</td>
          <td>${p.source || ""}</td>
          <td>${pill(p.status)}</td>
          <td>${p.word_count || 0}</td>
          <td><code>${p.path}</code></td>
        </tr>
      `).join("");
      els.status.textContent = "Configuracion cargada.";
    }

    function renderResults(data) {
      els.summary.innerHTML = `
        <article class="card"><span class="muted">Run</span><b>${data.run_id}</b></article>
        <article class="card"><span class="muted">Articulos</span><b>${data.paper_count}/${data.required_papers}</b></article>
        <article class="card"><span class="muted">Consultas</span><b>${data.results.length}</b></article>
        <article class="card"><span class="muted">Archivo</span><b>${data.output_path || ""}</b></article>
      `;

      els.results.innerHTML = data.results.map(r => `
        <tr>
          <td>${r.model_label}<br><code>${r.model_id}</code></td>
          <td>${r.prompt_name}</td>
          <td>${r.activity_name}</td>
          <td>${pill(r.status)}</td>
          <td>${r.elapsed_ms} ms</td>
          <td>
            ${r.error ? `<p class="pill bad">${r.error}</p>` : ""}
            <details open><summary>Ver respuesta</summary><pre>${(r.response || "").replace(/[&<>]/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[ch]))}</pre></details>
          </td>
        </tr>
      `).join("");
    }

    async function loadStatus() {
      const res = await fetch("/api/status");
      renderStatus(await res.json());
    }

    els.processBtn.addEventListener("click", async () => {
      els.processBtn.disabled = true;
      els.status.textContent = "Procesando PDFs localmente...";
      try {
        await fetch("/api/process-pdfs", { method: "POST" });
        await loadStatus();
        els.status.textContent = "PDFs procesados.";
      } catch (err) {
        els.status.textContent = `Error procesando PDFs: ${err.message}`;
      } finally {
        els.processBtn.disabled = false;
      }
    });

    els.runBtn.addEventListener("click", async () => {
      els.runBtn.disabled = true;
      els.status.textContent = els.mock.checked ? "Ejecutando simulacion..." : "Consultando Ollama. Puede tardar varios minutos.";
      try {
        const res = await fetch("/api/analyze", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
            model_id: els.model.value,
            prompt_id: els.prompt.value,
            activity_id: els.activity.value,
            mock: els.mock.checked,
          }),
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.detail || "Error desconocido");
        renderResults(data);
        els.status.textContent = "Analisis terminado.";
      } catch (err) {
        els.status.textContent = `Error: ${err.message}`;
      } finally {
        els.runBtn.disabled = false;
      }
    });

    loadStatus().catch(err => {
      els.status.textContent = `Error cargando configuracion: ${err.message}`;
    });
  </script>
</body>
</html>
"""
