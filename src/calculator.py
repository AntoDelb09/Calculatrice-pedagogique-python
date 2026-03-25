# calculator.py
# Ce module contient les fonctions de calcul de base.
# Il illustre les concepts de fonctions, paramètres et valeurs de retour en Python.

def add(a, b):
    """
    Additionne deux nombres.

    Paramètres:
    a (float): Premier nombre
    b (float): Deuxième nombre

    Retourne:
    float: La somme de a et b
    """
    return a + b

def subtract(a, b):
    """
    Soustrait b de a.

    Paramètres:
    a (float): Nombre duquel soustraire
    b (float): Nombre à soustraire

    Retourne:
    float: La différence a - b
    """
    return a - b

def multiply(a, b):
    """
    Multiplie deux nombres.

    Paramètres:
    a (float): Premier facteur
    b (float): Deuxième facteur

    Retourne:
    float: Le produit de a et b
    """
    return a * b

def divide(a, b):
    """
    Divise a par b.

    Paramètres:
    a (float): Dividende
    b (float): Diviseur (ne doit pas être zéro)

    Retourne:
    float: Le quotient a / b

    Lève:
    ValueError: Si b est zéro
    """
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b