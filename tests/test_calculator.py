# test_calculator.py
# Module de tests pour calculator.py
# Illustre l'importance des tests unitaires pour vérifier le comportement du code.

import unittest
from src.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    """
    Classe de tests pour les fonctions de calcul.
    Hérite de unittest.TestCase pour utiliser les méthodes d'assertion.
    """

    def test_add(self):
        """Test de la fonction add."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0.5, 0.5), 1.0)

    def test_subtract(self):
        """Test de la fonction subtract."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        """Test de la fonction multiply."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        """Test de la fonction divide."""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(5, 0)  # Test de l'exception pour division par zéro

if __name__ == "__main__":
    unittest.main()