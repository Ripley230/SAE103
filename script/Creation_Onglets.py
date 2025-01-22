from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QMainWindow

class Onglets(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Résultat de recherche des 'gros' fichiers...")
        self.setGeometry(200, 100, 1000, 700)

        # Créer un QTabWidget
        self.onglets = QTabWidget()
        self.setCentralWidget(self.onglets)

    def add_onglet(self, titre, layout_a_ajouter):
        # Création d'un onglet...
        onglet = QWidget()
        layout_onglet = QVBoxLayout()
        layout_onglet.addWidget(layout_a_ajouter)
        onglet.setLayout(layout_onglet)

        # Ajout de l'onglet au QTabWidget
        self.onglets.addTab(onglet, titre)

