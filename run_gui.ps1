# Script pour lancer l'interface graphique Tkinter avec WinPython
# Change vers le répertoire du projet
Push-Location $PSScriptRoot

# Chemin vers Python
$pythonPath = "C:\winpython_3x\python-3.7.0\python.exe"

# Lancer l'interface graphique
& $pythonPath src/calculator_gui.py

# Reviens au répertoire précédent
Pop-Location