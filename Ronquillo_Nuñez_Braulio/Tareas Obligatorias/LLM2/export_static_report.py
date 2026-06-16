from html import escape
from pathlib import Path

from SRC.analyzer import run_analysis
from SRC.config import load_config


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_DIR / "reporte_llm2_demo.html"


def render_table(report: dict) -> str:
    rows = []
    for item in report["results"]:
        rows.append(
            "<tr>"
            f"<td>{escape(item['model_label'])}<br><code>{escape(item['model_id'])}</code></td>"
            f"<td>{escape(item['prompt_name'])}</td>"
            f"<td>{escape(item['activity_name'])}</td>"
            f"<td><span class='pill {escape(item['status'])}'>{escape(item['status'])}</span></td>"
            f"<td>{item['elapsed_ms']} ms</td>"
            f"<td><pre>{escape(item.get('response') or item.get('error') or '')}</pre></td>"
            "</tr>"
        )
    return "\n".join(rows)


def main():
    config = load_config()
    report = run_analysis(
        config,
        model_id="all",
        prompt_id="all",
        activity_id="all",
        mock=True,
    )
    html = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LLM2 - Reporte demo</title>
  <style>
    body {{ margin: 0; background: #f5f7fb; color: #172033; font-family: Arial, sans-serif; }}
    main {{ width: min(1200px, calc(100% - 28px)); margin: 24px auto 48px; }}
    h1 {{ margin-bottom: 4px; }}
    .panel {{ background: white; border: 1px solid #d9e1ec; border-radius: 8px; padding: 16px; margin-bottom: 16px; }}
    .muted {{ color: #64748b; }}
    table {{ border-collapse: collapse; width: 100%; min-width: 900px; background: white; }}
    th, td {{ border-bottom: 1px solid #d9e1ec; padding: 10px; text-align: left; vertical-align: top; }}
    th {{ background: #f8fafc; color: #475569; }}
    .wrap {{ overflow-x: auto; }}
    pre {{ white-space: pre-wrap; max-height: 320px; overflow: auto; background: #f8fafc; padding: 10px; border-radius: 6px; }}
    .pill {{ display: inline-block; border-radius: 999px; padding: 3px 8px; font-weight: bold; background: #e2e8f0; }}
    .ok {{ background: #dcfce7; color: #047857; }}
    .fallback {{ background: #fef3c7; color: #b45309; }}
  </style>
</head>
<body>
  <main>
    <section class="panel">
      <h1>LLM2 - Reporte demo</h1>
      <p class="muted">Este HTML se abre sin servidor ni Ollama. Las respuestas son simuladas para mostrar el flujo de la tarea.</p>
      <p><b>Tema:</b> {escape(config['project']['topic'])}</p>
      <p><b>Planteamiento:</b> {escape(config['project']['problem_statement'])}</p>
      <p><b>Articulos procesados:</b> {report['paper_count']}/{report['required_papers']}</p>
      <p><b>Run:</b> {escape(report['run_id'])}</p>
    </section>
    <section class="panel wrap">
      <table>
        <thead>
          <tr><th>Modelo</th><th>Prompt</th><th>Actividad</th><th>Estado</th><th>Tiempo</th><th>Respuesta</th></tr>
        </thead>
        <tbody>
          {render_table(report)}
        </tbody>
      </table>
    </section>
  </main>
</body>
</html>"""
    OUTPUT_PATH.write_text(html, encoding="utf-8")
    print(f"Reporte generado: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
