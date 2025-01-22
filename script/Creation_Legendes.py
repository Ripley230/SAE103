from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QCheckBox
from PyQt5.QtCore import Qt

class Legendes:
    def __init__(self, liste_fichiers, liste_couleurs, num_legende_start):
        self.liste_fichiers = liste_fichiers
        self.liste_couleurs = liste_couleurs
        self.num_legende_start = num_legende_start
        self.num_legende_stop = min(len(liste_fichiers), num_legende_start+25)
        self.cases_a_cocher = []
    def dessine_legendes(self):
        """
        Retourne une Widget Layout PyQt contenant une liste de légendes.
        """
        legendes = QWidget()
        layout_legendes = QVBoxLayout(legendes)
        layout_legendes.setContentsMargins(0, 20, 0, 20)
        layout_legendes.setAlignment(Qt.AlignTop)

# Ajouter des datas à chaque légende
        for num_slice in range(self.num_legende_start, self.num_legende_stop):

            # Création de la case à cocher
            case_a_cocher = QCheckBox()
            case_a_cocher.setChecked(False) # Définir l'état initial de la case (cochée ou non)
            self.cases_a_cocher.append(case_a_cocher)

            # Création d'un petit carré coloré
            rectangle_colore = QWidget()
            rectangle_colore.setFixedSize(16, 16)
            couleur = self.liste_couleurs[num_slice].name()
            rectangle_colore.setStyleSheet(f"background-color: {couleur}; border: 1px solid black;")

            # composition du contenu textuel de la légende
            chemin_fichier = self.liste_fichiers[num_slice][0] # Extrait le chemin et nom du fichier
            taille_fichier = self.liste_fichiers[num_slice][1] // 1048576 # Extrait la taille du fichier
            etiquette_legende = f"<span style='color:black;font-family:Arial Narrow'>{chemin_fichier} -->
                (</span><span style='color:red;'>{taille_fichier} Mo</span>)"
            texte_legende = QLabel(etiquette_legende)

            # Disposition horizontale pour l'élément de légende
            ligne_legende = QHBoxLayout()
            ligne_legende.setAlignment(Qt.AlignLeft)
            ligne_legende.setContentsMargins(5, 0, 5, 5)
            ligne_legende.stretch(2)
            ligne_legende.addWidget(case_a_cocher)
            ligne_legende.addWidget(rectangle_colore)
            ligne_legende.addWidget(texte_legende)

            legende = QWidget()
            legende.setLayout(ligne_legende)
            legende.setContentsMargins(0, 0, 0, 0)

            layout_legendes.addWidget(legende)
            layout_legendes.setSpacing(0)

        return legendes

    def recupere_etats_case_a_cocher(self):
        etats = []
        for case in self.cases_a_cocher:
            etats.append(case.isChecked())
        return etats