# main.py
# Point d'entrée principal du programme.
# Illustre l'importation de modules, les boucles, les conditionnelles et la gestion des erreurs.

from calculator import add, subtract, multiply, divide

def main():
    """
    Fonction principale qui gère l'interface en ligne de commande.
    """
    print("Bienvenue dans la calculatrice pédagogique Python!")
    print("Opérations disponibles: +, -, *, /")
    print("Tapez 'quit' pour quitter.")

    while True:  # Boucle infinie jusqu'à ce que l'utilisateur quitte
        try:
            # Demander l'opération
            operation = input("Entrez l'opération (+, -, *, /) ou 'quit': ").strip()
            if operation.lower() == 'quit':
                print("Au revoir!")
                break

            if operation not in ['+', '-', '*', '/']:
                print("Opération invalide. Réessayez.")
                continue

            # Demander les nombres
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))

            # Effectuer le calcul selon l'opération
            if operation == '+':
                result = add(a, b)
            elif operation == '-':
                result = subtract(a, b)
            elif operation == '*':
                result = multiply(a, b)
            elif operation == '/':
                result = divide(a, b)

            print(f"Résultat: {a} {operation} {b} = {result}")

        except ValueError as e:
            print(f"Erreur: {e}")
        except Exception as e:
            print(f"Erreur inattendue: {e}")

if __name__ == "__main__":
    # Cette condition permet d'exécuter main() seulement si le script est lancé directement,
    # pas s'il est importé comme module.
    main()