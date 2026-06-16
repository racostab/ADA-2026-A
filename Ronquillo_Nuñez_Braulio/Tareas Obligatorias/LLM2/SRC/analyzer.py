from datetime import datetime
import json
from pathlib import Path
import uuid

from .config import OUTPUTS_DIR, ensure_dirs, load_prompt_templates
from .ollama_client import ask_ollama
from .pdf_processor import load_processed_papers


def build_papers_context(processed: dict, max_chars_per_paper: int = 4500) -> str:
    chunks = []
    for paper in processed.get("papers", []):
        if paper.get("status") != "ok":
            continue
        text_path = Path(paper["text_path"])
        text = text_path.read_text(encoding="utf-8")
        if len(text) > max_chars_per_paper:
            text = text[:max_chars_per_paper].rsplit(" ", 1)[0] + "..."
        chunks.append(
            "\n".join(
                [
                    f"ARTICULO: {paper.get('title', paper.get('id'))}",
                    f"FUENTE: {paper.get('source', 'N/D')}",
                    f"PALABRAS_EXTRAIDAS: {paper.get('word_count', 0)}",
                    "EXTRACTO:",
                    text,
                ]
            )
        )
    return "\n\n---\n\n".join(chunks)


def format_prompt(template: str, config: dict, activity: dict, papers_context: str, paper_count: int) -> str:
    project = config["project"]
    return template.format(
        topic=project["topic"],
        problem_statement=project["problem_statement"],
        language=project.get("language", "es"),
        required_paper_count=project.get("required_papers", 4),
        paper_count=paper_count,
        activity_name=activity["name"],
        activity_prompt=activity["prompt"],
        papers_context=papers_context,
    )


def find_by_id(items: list[dict], item_id: str) -> dict:
    for item in items:
        if item["id"] == item_id:
            return item
    raise KeyError(item_id)


def expand_selection(items: list[dict], selected: str) -> list[dict]:
    if selected == "all":
        return items
    return [find_by_id(items, selected)]


def demo_response(config: dict, activity: dict, paper_count: int, original_error: str = "") -> str:
    topic = config["project"]["topic"]
    problem = config["project"]["problem_statement"]
    required = config["project"].get("required_papers", 4)
    missing_note = (
        f"Actualmente hay {paper_count}/{required} articulos; falta al menos un articulo para cumplir la consigna."
        if paper_count < required
        else f"Hay {paper_count}/{required} articulos requeridos."
    )
    error_note = f"\n\nAviso tecnico: no se ejecuto Ollama. Motivo: {original_error}" if original_error else ""

    return (
        "Respuesta demo generada por el sistema local de respaldo.\n\n"
        f"Tema: {topic}\n"
        f"Planteamiento: {problem}\n\n"
        f"Actividad: {activity['name']}\n"
        f"{activity['prompt']}\n\n"
        "Tabla resumida:\n"
        "| Eje | Observacion | Uso en la tesis |\n"
        "|---|---|---|\n"
        "| Redes complejas | Los articulos apoyan representar unidades linguisticas como nodos y relaciones de similitud como aristas. | Construir redes lexicas, ortograficas o fonologicas de lenguas indigenas. |\n"
        "| Descriptores | Se pueden extraer grado, clustering, caminos, modularidad, componentes y medidas globales. | Formar vectores de caracteristicas por lengua o corpus. |\n"
        "| Nube de puntos | Los vectores de metricas permiten comparar lenguas en un espacio de descriptores. | Evaluar similitud, agrupamientos y separacion entre lenguas. |\n"
        "| TDA/SCAE | El articulo SCAE sugiere usar complejos simpliciales para caracterizar irregularidad y estructura. | Aplicar SCAE o filtraciones sobre la nube de puntos de metricas. |\n\n"
        "Conclusion preliminar: el problema es pertinente y viable con cambios, siempre que se delimite el corpus, "
        "se definan las unidades linguisticas y se agregue un cuarto articulo de soporte.\n\n"
        f"{missing_note}"
        f"{error_note}"
    )


def run_analysis(config: dict, model_id: str, prompt_id: str, activity_id: str, mock: bool = False) -> dict:
    ensure_dirs()
    processed = load_processed_papers(config)
    prompts = load_prompt_templates()
    models = config["models"]
    activities = config["activities"]

    selected_models = expand_selection(models, model_id)
    selected_prompts = expand_selection(prompts, prompt_id)
    selected_activities = expand_selection(activities, activity_id)
    papers_context = build_papers_context(processed)
    ok_papers = [paper for paper in processed.get("papers", []) if paper.get("status") == "ok"]

    results = []
    run_id = datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:8]
    base_url = config["ollama"]["base_url"]
    timeout = int(config["ollama"].get("timeout_seconds", 180))
    fallback_to_demo = bool(config["ollama"].get("fallback_to_demo", False))

    for model in selected_models:
        for prompt in selected_prompts:
            for activity in selected_activities:
                full_prompt = format_prompt(
                    prompt["template"],
                    config,
                    activity,
                    papers_context,
                    len(ok_papers),
                )
                started = datetime.now()
                status = "ok"
                response = ""
                error = ""

                try:
                    if mock:
                        response = demo_response(config, activity, len(ok_papers))
                    else:
                        response = ask_ollama(base_url, model["id"], full_prompt, timeout)
                except Exception as exc:
                    error = str(exc)
                    if fallback_to_demo:
                        status = "fallback"
                        response = demo_response(config, activity, len(ok_papers), error)
                    else:
                        status = "error"

                elapsed_ms = round((datetime.now() - started).total_seconds() * 1000, 2)
                results.append(
                    {
                        "run_id": run_id,
                        "created_at": started.strftime("%Y-%m-%d %H:%M:%S"),
                        "model_id": model["id"],
                        "model_label": model.get("label", model["id"]),
                        "prompt_id": prompt["id"],
                        "prompt_name": prompt["name"],
                        "activity_id": activity["id"],
                        "activity_name": activity["name"],
                        "status": status,
                        "elapsed_ms": elapsed_ms,
                        "response": response,
                        "error": error,
                    }
                )

    report = {
        "run_id": run_id,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "paper_count": len(ok_papers),
        "required_papers": config["project"].get("required_papers", 4),
        "results": results,
    }
    output_path = OUTPUTS_DIR / f"analysis_{run_id}.json"
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    report["output_path"] = str(output_path)
    return report
