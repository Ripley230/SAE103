from pathlib import Path
from PyQt5.QtWidgets import QApplication, QFileDialog


def selectionner_repertoire():
    app = QApplication([])
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.ShowDirsOnly, True)

    if dialog.exec_():
        repertoire_selectionne = dialog.selectedFiles()[0]
        return str(Path(repertoire_selectionne))

    return None


if __name__ == "__main__":
    repertoire_base = selectionner_repertoire()
    print(repertoire_base)
