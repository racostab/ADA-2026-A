from pathlib import Path
from threading import Timer
import os
import webbrowser

import uvicorn


def open_browser():
    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent
    os.chdir(project_root)
    Timer(1.2, open_browser).start()
    uvicorn.run("SRC.api:app", host="127.0.0.1", port=8000, reload=False)
