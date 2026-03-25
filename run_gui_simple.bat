@echo off
REM Script pour lancer l'interface graphique Tkinter simplifiée avec WinPython

REM Aller dans le répertoire du script
cd /d "%~dp0"

REM Lancer l'interface graphique simplifiée avec chemin absolu
"S:\Technofan\Blagnac\R&D\BE\01_BE_ELEC\15_Suivi_Outils_Metier_FPGA\ITG\Standards_VHDL\winpython_3x\python-3.7.0\python.exe" "%~dp0src\calculator_gui_simple_tk.py"

pause