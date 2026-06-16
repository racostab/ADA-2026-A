from pathlib import Path
import json
import re
import shutil
import subprocess

from .config import PROCESSED_DIR, ensure_dirs


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_with_pypdf(path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)


def extract_with_pdftotext(path: Path) -> str:
    if shutil.which("pdftotext") is None:
        raise RuntimeError("No esta disponible pdftotext.")

    result = subprocess.run(
        ["pdftotext", str(path), "-"],
        text=True,
        capture_output=True,
        timeout=60,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "pdftotext fallo.")
    return result.stdout


def extract_pdf_text(path: Path) -> str:
    try:
        return normalize_text(extract_with_pypdf(path))
    except Exception:
        return normalize_text(extract_with_pdftotext(path))


def paper_excerpt(text: str, limit: int = 1200) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0] + "..."


def process_papers(config: dict) -> dict:
    ensure_dirs()
    papers = []

    for paper in config.get("papers", []):
        item = dict(paper)
        path = Path(item["path"]).expanduser()
        item["exists"] = path.exists()

        if not path.exists():
            item["status"] = "missing"
            item["word_count"] = 0
            item["text_path"] = ""
            item["excerpt"] = ""
            papers.append(item)
            continue

        try:
            text = extract_pdf_text(path)
            text_path = PROCESSED_DIR / f"{item['id']}.txt"
            text_path.write_text(text, encoding="utf-8")
            item["status"] = "ok"
            item["word_count"] = len(text.split())
            item["char_count"] = len(text)
            item["text_path"] = str(text_path)
            item["excerpt"] = paper_excerpt(text)
        except Exception as exc:
            item["status"] = "error"
            item["error"] = str(exc)
            item["word_count"] = 0
            item["text_path"] = ""
            item["excerpt"] = ""

        papers.append(item)

    report = {
        "paper_count": len(papers),
        "required_papers": config.get("project", {}).get("required_papers", 4),
        "papers": papers,
    }
    (PROCESSED_DIR / "papers.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return report


def load_processed_papers(config: dict) -> dict:
    report_path = PROCESSED_DIR / "papers.json"
    if report_path.exists():
        return json.loads(report_path.read_text(encoding="utf-8"))
    return process_papers(config)
