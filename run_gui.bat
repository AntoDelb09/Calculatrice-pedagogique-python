@echo off
REM Script pour lancer l'interface graphique Tkinter avec WinPython
cd /d "%~dp0"

REM Chemin vers Python
set PYTHON_PATH=C:\winpython_3x\python-3.7.0\python.exe

REM Lancer l'interface graphique
"%PYTHON_PATH%" src/calculator_gui.py

pause