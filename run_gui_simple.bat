@echo off
REM Script pour lancer l'interface graphique Tkinter simplifiée avec WinPython
cd /d "%~dp0"

REM Chemin vers Python
set PYTHON_PATH=S:\Technofan\Blagnac\R&D\BE\01_BE_ELEC\15_Suivi_Outils_Metier_FPGA\ITG\Standards_VHDL\winpython_3x\python-3.7.0\python.exe

REM Lancer l'interface graphique simplifiée
"%PYTHON_PATH%" src/calculator_gui_simple_tk.py

pause