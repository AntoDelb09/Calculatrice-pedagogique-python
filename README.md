# Projet Pédagogique Python - Calculatrice

Ce projet est une calculatrice en ligne de commande simple conçue pour enseigner les concepts de base de Python.

## Structure du Projet

- `src/`: Code source principal
  - `calculator.py`: Fonctions de calcul de base
  - `main.py`: Interface utilisateur en ligne de commande
- `tests/`: Tests unitaires
  - `test_calculator.py`: Tests pour les fonctions de calcul
- `requirements.txt`: Dépendances (vide pour ce projet)

## Interfaces Graphiques Disponibles

### Interface Tkinter Simplifiée (Recommandée - Compatible avec WinPython)
```bash
# Double-cliquez sur run_gui_simple.bat
# ou en PowerShell
.\run_gui_simple.ps1
```

Caractéristiques :
- ✅ Aucune installation supplémentaire
- ✅ Interface claire et simple
- ✅ Buttons Calculer et Effacer
- ✅ Gestion complète des erreurs

## Concepts Python Illustrés

- **Fonctions**: Définition, paramètres, valeurs de retour, docstrings
- **Modules et Imports**: Importation de fonctions depuis d'autres modules
- **Boucles**: Boucle while pour l'interaction continue
- **Conditionnelles**: if/elif/else pour la logique
- **Gestion d'Erreurs**: try/except pour les exceptions
- **Tests Unitaires**: Utilisation de unittest pour vérifier le code
- **Point d'Entrée**: if __name__ == "__main__"
- **Interfaces Graphiques**: Tkinter et PySimpleGUI pour l'interface utilisateur

## Installation

1. Assurez-vous d'avoir Python 3 installé (ou WinPython).
2. Clonez ou téléchargez ce projet.

## Utilisation avec WinPython

Si vous utilisez WinPython, trois méthodes sont disponibles :

### Méthode 1: Utiliser le script batch (Windows CMD)
```bash
run_calculator.bat
```

### Méthode 2: Utiliser le script PowerShell
```powershell
.\run_calculator.ps1
```
*Note: Si vous avez une erreur de politique d'exécution PowerShell, exécutez d'abord:*
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Méthode 3: Utiliser la tâche VS Code
1. Appuyez sur `Ctrl+Shift+P` pour ouvrir la palette de commandes
2. Tapez "Tasks: Run Task"
3. Sélectionnez "Run Calculator"

### Méthode 4: Exécuter les tests
Pour exécuter les tests unitaires :
```powershell
.\run_tests.ps1
```
Ou via la tâche VS Code : "Run Tests"

Suivez les instructions à l'écran pour effectuer des calculs.

## Exemples

```
Bienvenue dans la calculatrice pédagogique Python!
Opérations disponibles: +, -, *, /
Tapez 'quit' pour quitter.
Entrez l'opération (+, -, *, /) ou 'quit': +
Entrez le premier nombre: 5
Entrez le deuxième nombre: 3
Résultat: 5.0 + 3.0 = 8.0
```

## Améliorations Possibles

- Ajouter plus d'opérations (puissance, racine carrée)
- Interface graphique avec Tkinter
- Support pour des expressions mathématiques complexes
- Historique des calculs