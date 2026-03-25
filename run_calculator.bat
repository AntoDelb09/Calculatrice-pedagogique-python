@echo off
REM Script pour exécuter le projet avec WinPython
cd /d "%~dp0"

REM Chemin vers Python
set PYTHON_PATH=C:\winpython_3x\python-3.7.0\python.exe

REM Exécute la calculatrice
"%PYTHON_PATH%" src/main.py

pause
