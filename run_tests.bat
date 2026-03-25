@echo off
REM Script pour exécuter les tests avec WinPython
cd /d "%~dp0"

REM Chemin vers Python
set PYTHON_PATH=C:\winpython_3x\python-3.7.0\python.exe

REM Exécute les tests
"%PYTHON_PATH%" -m unittest tests.test_calculator

pause
