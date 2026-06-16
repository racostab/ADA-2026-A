@echo off
cd /d "%~dp0"
python -m pip install pyinstaller
python -m PyInstaller --onefile --name API_Claude_Dashboard --add-data "DAT;DAT" --add-data "SRC;SRC" run_dashboard.py
echo.
echo Ejecutable generado en dist\API_Claude_Dashboard.exe
pause
