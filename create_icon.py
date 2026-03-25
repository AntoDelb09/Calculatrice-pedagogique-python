# create_simple_icon.py - Version ultra-simplifiée
# Ce script crée une icône basique en copiant une icône système

import shutil
import os

def create_simple_icon():
    # Chemins vers des icônes système Windows
    system_icons = [
        r"C:\Windows\System32\calc.exe",  # L'exécutable de la calculatrice Windows
        r"C:\Windows\System32\shell32.dll",  # DLL avec des icônes système
    ]

    target_path = "calculator_icon.ico"

    # Essayer de copier l'icône de la calculatrice système
    for icon_source in system_icons:
        if os.path.exists(icon_source):
            try:
                # Pour une vraie icône, il faudrait extraire l'icône de l'exécutable
                # Mais pour l'instant, créons un fichier placeholder
                print(f"Source d'icône trouvée : {icon_source}")
                print("Pour créer une vraie icône personnalisée :")
                print("1. Ouvrez Paint ou un éditeur d'images")
                print("2. Créez une image 256x256 pixels")
                print("3. Dessinez un symbole de calculatrice")
                print("4. Sauvegardez en PNG puis convertissez en ICO")
                print("5. Ou utilisez un outil en ligne comme https://favicon.io/favicon-converter/")

                # Créer un fichier texte avec des instructions
                with open("icon_instructions.txt", "w", encoding="utf-8") as f:
                    f.write("""INSTRUCTIONS POUR CRÉER UNE ICÔNE PERSONNALISÉE :

1. Ouvrez Microsoft Paint ou un éditeur d'images
2. Créez une nouvelle image de 256x256 pixels
3. Dessinez un rectangle blanc avec une bordure noire
4. Ajoutez le texte "CALC" en bleu au centre
5. Ajoutez les symboles "+ - × ÷" en gris dessous
6. Sauvegardez l'image en PNG
7. Allez sur https://favicon.io/favicon-converter/
8. Téléchargez votre PNG et convertissez-le en ICO
9. Renommez le fichier en "calculator_icon.ico"
10. Placez-le dans ce dossier

Ou utilisez l'icône par défaut de Windows pour le raccourci.
""")

                print("Fichier d'instructions créé : icon_instructions.txt")
                return True

            except Exception as e:
                print(f"Erreur lors de la copie : {e}")
                continue

    print("Aucune source d'icône système trouvée.")
    print("Utilisez les instructions dans icon_instructions.txt")

if __name__ == "__main__":
    print("Création d'instructions pour l'icône de la calculatrice...")
    create_simple_icon()