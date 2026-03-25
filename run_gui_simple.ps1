# Script pour lancer l'interface graphique Tkinter simplifiée avec WinPython
# Change vers le répertoire du projet
Push-Location $PSScriptRoot

# Lancer l'interface graphique simplifiée directement avec le chemin complet
& "S:\Technofan\Blagnac\R&D\BE\01_BE_ELEC\15_Suivi_Outils_Metier_FPGA\ITG\Standards_VHDL\winpython_3x\python-3.7.0\python.exe" src/calculator_gui_simple_tk.py

# Reviens au répertoire précédent
Pop-Location