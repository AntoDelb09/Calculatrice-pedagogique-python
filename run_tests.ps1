# Script pour exécuter les tests avec WinPython
# Change vers le répertoire du projet
Push-Location $PSScriptRoot

# Chemin vers Python
$pythonPath = "C:\winpython_3x\python-3.7.0\python.exe"

# Exécute les tests
& $pythonPath -m unittest tests.test_calculator

# Reviens au répertoire précédent
Pop-Location
