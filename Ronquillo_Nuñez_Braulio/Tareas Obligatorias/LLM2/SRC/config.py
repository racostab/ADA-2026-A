from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config.json"
PROMPTS_DIR = BASE_DIR / "DAT" / "prompts"
PROCESSED_DIR = BASE_DIR / "DAT" / "processed"
OUTPUTS_DIR = BASE_DIR / "DAT" / "outputs"


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def load_prompt_templates() -> list[dict]:
    prompts = []
    for path in sorted(PROMPTS_DIR.glob("*.txt")):
        prompts.append(
            {
                "id": path.stem,
                "name": path.stem.replace("_", " ").title(),
                "template": path.read_text(encoding="utf-8"),
            }
        )
    return prompts


def ensure_dirs() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
