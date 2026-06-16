from pathlib import Path
from threading import Timer
import os
import webbrowser

import uvicorn


def open_browser():
    webbrowser.open("http://127.0.0.1:8010")


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    os.chdir(base_dir)
    Timer(1.2, open_browser).start()
    uvicorn.run("SRC.app:app", host="127.0.0.1", port=8010, reload=False)
