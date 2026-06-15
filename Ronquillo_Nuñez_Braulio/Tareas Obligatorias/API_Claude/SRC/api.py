from pathlib import Path

import anthropic
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from .evaluador_dashboard import ALGORITHMS, DEFAULT_MODEL, run_evaluation


PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

app = FastAPI(title="API Claude Evaluador", version="2.0.0")


class ChatRequest(BaseModel):
    prompt: str
    model: str = DEFAULT_MODEL
    max_tokens: int = 300


class EvaluationRequest(BaseModel):
    algorithm: str = Field(default="all", description="all, maze o stupid_sort")
    attempts: int = Field(default=10, ge=1, le=10)
    model: str = DEFAULT_MODEL
    mock: bool = Field(default=False, description="Usa soluciones locales para probar el tablero sin llamar a Claude.")


def get_client():
    import os

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="No se encontro ANTHROPIC_API_KEY en API_Claude/.env",
        )

    return anthropic.Anthropic(api_key=api_key)


def extract_text(message) -> str:
    text = ""
    for block in message.content:
        if getattr(block, "type", None) == "text":
            text += block.text
    return text


@app.get("/", response_class=HTMLResponse)
def dashboard():
    return HTMLResponse(DASHBOARD_HTML)


@app.get("/health")
def health():
    import os

    return {
        "ok": True,
        "servicio": "API Claude Evaluador",
        "anthropic_key": bool(os.getenv("ANTHROPIC_API_KEY")),
        "algorithms": list(ALGORITHMS.keys()),
    }


@app.post("/api/chat")
def chat(req: ChatRequest):
    try:
        client = get_client()
        message = client.messages.create(
            model=req.model,
            max_tokens=req.max_tokens,
            messages=[{"role": "user", "content": req.prompt}],
        )

        return {"model": req.model, "response": extract_text(message)}

    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/api/evaluate")
def evaluate(req: EvaluationRequest):
    if req.algorithm == "all":
        algorithms = ["maze", "stupid_sort"]
    elif req.algorithm in ALGORITHMS:
        algorithms = [req.algorithm]
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Algoritmo no soportado: {req.algorithm}",
        )

    try:
        client = None if req.mock else get_client()
        return run_evaluation(
            algorithms=algorithms,
            attempts=req.attempts,
            client=client,
            model=req.model,
            mock=req.mock,
        )
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


DASHBOARD_HTML = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Evaluador Claude - Maze y Stupid Sort</title>
  <style>
    :root {
      color-scheme: light;
      --bg: #f5f7fb;
      --panel: #ffffff;
      --ink: #172033;
      --muted: #64748b;
      --line: #d9e1ec;
      --accent: #6b4bb7;
      --accent-2: #0f766e;
      --bad: #b91c1c;
      --warn: #b45309;
      --good: #047857;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    body {
      margin: 0;
      background: var(--bg);
      color: var(--ink);
    }

    header {
      background: var(--panel);
      border-bottom: 1px solid var(--line);
      padding: 18px 24px;
      position: sticky;
      top: 0;
      z-index: 1;
    }

    main {
      width: min(1180px, calc(100% - 32px));
      margin: 24px auto 48px;
    }

    h1 {
      margin: 0;
      font-size: 24px;
    }

    h2 {
      font-size: 18px;
      margin: 0 0 14px;
    }

    .subtitle {
      color: var(--muted);
      margin: 6px 0 0;
      font-size: 14px;
    }

    .toolbar, .panel {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }

    .toolbar {
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 12px;
      align-items: end;
      margin-bottom: 18px;
    }

    label {
      display: grid;
      gap: 6px;
      font-size: 13px;
      color: var(--muted);
      font-weight: 600;
    }

    select, input {
      min-height: 38px;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 0 10px;
      font: inherit;
      color: var(--ink);
      background: #fff;
    }

    .check {
      display: flex;
      align-items: center;
      gap: 8px;
      min-height: 38px;
    }

    .check input {
      min-height: auto;
      width: 18px;
      height: 18px;
    }

    button {
      min-height: 40px;
      border: 0;
      border-radius: 6px;
      background: var(--accent);
      color: white;
      font-weight: 700;
      cursor: pointer;
      padding: 0 14px;
    }

    button:disabled {
      opacity: 0.55;
      cursor: wait;
    }

    .grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 12px;
    }

    .metric {
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      background: #fbfdff;
    }

    .metric b {
      display: block;
      font-size: 22px;
      margin-top: 6px;
    }

    .muted {
      color: var(--muted);
    }

    .status {
      margin: 12px 0 18px;
      color: var(--muted);
      min-height: 22px;
    }

    .table-wrap {
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
    }

    table {
      border-collapse: collapse;
      width: 100%;
      min-width: 820px;
      background: white;
    }

    th, td {
      padding: 10px 12px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      font-size: 14px;
      vertical-align: top;
    }

    th {
      background: #f8fafc;
      color: #475569;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    tr:last-child td {
      border-bottom: 0;
    }

    .pill {
      display: inline-block;
      border-radius: 999px;
      padding: 3px 8px;
      font-size: 12px;
      font-weight: 700;
      background: #e2e8f0;
      color: #334155;
      white-space: nowrap;
    }

    .pill.good { background: #dcfce7; color: var(--good); }
    .pill.warn { background: #fef3c7; color: var(--warn); }
    .pill.bad { background: #fee2e2; color: var(--bad); }

    details {
      color: var(--muted);
    }

    code {
      background: #eef2ff;
      padding: 2px 5px;
      border-radius: 4px;
    }

    footer {
      color: var(--muted);
      font-size: 13px;
      margin-top: 18px;
      line-height: 1.5;
    }

    @media (max-width: 760px) {
      header { padding: 14px 16px; }
      main { width: min(100% - 20px, 1180px); margin-top: 14px; }
      .toolbar { grid-template-columns: 1fr; }
      h1 { font-size: 20px; }
      table { min-width: 720px; }
    }
  </style>
</head>
<body>
  <header>
    <h1>Evaluador Claude</h1>
    <p class="subtitle">10 realizaciones para Maze y Stupid/Gnome Sort, con tabla de @3, @5, pass@3 y pass@5.</p>
  </header>

  <main>
    <section class="toolbar">
      <label>Algoritmo
        <select id="algorithm">
          <option value="all">Maze + Stupid Sort</option>
          <option value="maze">Maze</option>
          <option value="stupid_sort">Stupid/Gnome Sort</option>
        </select>
      </label>
      <label>Realizaciones
        <input id="attempts" type="number" min="1" max="10" value="10">
      </label>
      <label>Modelo
        <input id="model" value="claude-sonnet-4-5">
      </label>
      <label class="check">
        <input id="mock" type="checkbox">
        Simular sin Claude
      </label>
      <button id="runBtn">Ejecutar evaluación</button>
    </section>

    <p class="status" id="status">Listo. Usa "Simular sin Claude" para probar el tablero sin consumir API.</p>

    <section class="grid">
      <div class="panel">
        <h2>Resumen</h2>
        <div id="summary" class="cards"></div>
      </div>

      <div class="panel">
        <h2>Resultados por realización</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Algoritmo</th>
                <th>#</th>
                <th>Grado</th>
                <th>@3</th>
                <th>@5</th>
                <th>Tiempo</th>
                <th>Archivos</th>
                <th>Detalle</th>
              </tr>
            </thead>
            <tbody id="results">
              <tr><td colspan="8" class="muted">Todavía no hay ejecuciones.</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <footer>
      <p><b>Interpretación:</b> <code>@3</code> pasa casos oficiales/básicos; <code>@5</code> pasa oficiales y borde. <code>pass@3</code> y <code>pass@5</code> se calculan sobre las realizaciones que alcanzan <code>@5</code>, usando la estimación combinatoria habitual de evaluación de código generado.</p>
      <p>Los archivos generados se guardan en <code>API_Claude/DAT/runs/</code>.</p>
    </footer>
  </main>

  <script>
    const runBtn = document.getElementById("runBtn");
    const statusEl = document.getElementById("status");
    const summaryEl = document.getElementById("summary");
    const resultsEl = document.getElementById("results");

    function gradeClass(grade) {
      if (grade === "@5") return "good";
      if (grade === "@3") return "warn";
      return "bad";
    }

    function pct(value) {
      return `${Math.round(value * 100)}%`;
    }

    function renderSummary(summaries) {
      if (!summaries.length) {
        summaryEl.innerHTML = '<p class="muted">Sin resumen.</p>';
        return;
      }
      summaryEl.innerHTML = summaries.map(item => `
        <article class="metric">
          <span class="muted">${item.algorithm_title}</span>
          <b>${item.at5_correct}/${item.attempts} @5</b>
          <div>@3: ${item.at3_correct}/${item.attempts} (${pct(item.at3_rate)})</div>
          <div>pass@3: ${pct(item.pass_at_3)}</div>
          <div>pass@5: ${pct(item.pass_at_5)}</div>
        </article>
      `).join("");
    }

    function renderDetails(tests) {
      if (!tests || !tests.length) return '<span class="muted">Sin pruebas.</span>';
      const rows = tests.map(test => {
        const cls = test.ok ? "good" : "bad";
        const text = test.ok ? "OK" : "FALLO";
        return `<li><span class="pill ${cls}">${text}</span> ${test.level} - ${test.label}: ${test.message || ""}</li>`;
      }).join("");
      return `<details><summary>Ver pruebas</summary><ul>${rows}</ul></details>`;
    }

    function renderResults(results) {
      if (!results.length) {
        resultsEl.innerHTML = '<tr><td colspan="8" class="muted">Sin resultados.</td></tr>';
        return;
      }
      resultsEl.innerHTML = results.map(item => `
        <tr>
          <td>${item.algorithm_title}</td>
          <td>${item.attempt}</td>
          <td><span class="pill ${gradeClass(item.grade)}">${item.grade}</span></td>
          <td>${item.at3_passed}/${item.at3_total}</td>
          <td>${item.at5_passed}/${item.at5_total}</td>
          <td>${item.elapsed_ms} ms</td>
          <td>
            ${item.program_path ? `<code>${item.program_path}</code>` : ""}
            ${item.error ? `<span class="pill bad">${item.error}</span>` : ""}
          </td>
          <td>${renderDetails(item.tests)}</td>
        </tr>
      `).join("");
    }

    runBtn.addEventListener("click", async () => {
      const payload = {
        algorithm: document.getElementById("algorithm").value,
        attempts: Number(document.getElementById("attempts").value || 10),
        model: document.getElementById("model").value || "claude-sonnet-4-5",
        mock: document.getElementById("mock").checked,
      };

      runBtn.disabled = true;
      statusEl.textContent = payload.mock
        ? "Ejecutando simulación local..."
        : "Consultando Claude y evaluando soluciones. Esto puede tardar varios minutos.";

      try {
        const response = await fetch("/api/evaluate", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify(payload),
        });

        const data = await response.json();
        if (!response.ok) {
          throw new Error(data.detail || "Error desconocido");
        }

        statusEl.textContent = `Run ${data.run_id} terminado (${data.created_at}).`;
        renderSummary(data.summaries);
        renderResults(data.results);
      } catch (error) {
        statusEl.textContent = `Error: ${error.message}`;
      } finally {
        runBtn.disabled = false;
      }
    });
  </script>
</body>
</html>
"""
