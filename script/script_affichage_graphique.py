import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor
import random
import sys

from Creation_Onglets import Onglets
from Creation_Camembert import Camembert
from Creation_Legendes import Legendes
from Creation_Boutons import Boutons


def charger_donnees(fichier_json):
    with open(fichier_json, 'r', encoding='utf-8') as f:
        return json.load(f)


def generer_couleurs(nb_couleurs):
    return [QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(nb_couleurs)]


def callback_generer_script():
    print("Génération du script PowerShell (à implémenter)")


def main():
    app = QApplication(sys.argv)
    fenetre = QMainWindow()

    onglets = Onglets()

    donnees = charger_donnees('gros_fichiers.json')

    tailles = [fichier[1] for fichier in donnees]
    labels = [fichier[0] for fichier in donnees]

    couleurs = generer_couleurs(len(donnees))

    camembert = Camembert(tailles, labels, couleurs)
    onglets.addTab(camembert, "Camembert")

    for i in range(0, len(donnees), 25):
        page_legendes = Legendes(donnees[i:i + 25], couleurs[i:i + 25])
        onglets.addTab(page_legendes, f"Légendes {i // 25 + 1}")

    boutons = Boutons(callback_generer_script)
    onglets.addTab(boutons, "Actions")

    layout = QVBoxLayout()
    layout.addWidget(onglets)

    widget_central = QWidget()
    widget_central.setLayout(layout)

    fenetre.setCentralWidget(widget_central)

    fenetre.setWindowTitle("Analyse des gros fichiers")
    fenetre.setGeometry(100, 100, 800, 600)

    fenetre.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
