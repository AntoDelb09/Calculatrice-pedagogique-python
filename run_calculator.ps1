# Script pour exécuter le projet avec WinPython
# Change vers le répertoire du projet
Push-Location $PSScriptRoot

# Chemin vers Python
$pythonPath = "C:\winpython_3x\python-3.7.0\python.exe"

# Exécute la calculatrice
& $pythonPath src/main.py

# Reviens au répertoire précédent
Pop-Location
