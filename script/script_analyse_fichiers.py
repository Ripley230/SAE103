from pathlib import Path
import json
import sys


def construire_liste_fichiers(repertoire_de_base):
    liste_fichiers = []
    repertoire = Path(repertoire_de_base)

    for fichier in repertoire.rglob('*'):
        if fichier.is_file():
            taille = fichier.stat().st_size
            liste_fichiers.append([str(fichier), taille])

    return liste_fichiers


def trier_liste_fichiers(liste_fichiers):
    return sorted(liste_fichiers, key=lambda x: x[1], reverse=True)


def filtrer_gros_fichiers(liste_fichiers, taille_mini_mo, nb_maxi_fichiers):
    taille_mini_octets = taille_mini_mo * 1048576  # Convertir Mo en octets
    return [f for f in liste_fichiers if f[1] >= taille_mini_octets][:nb_maxi_fichiers]


def sauvegarder_json(liste_fichiers, nom_fichier):
    for liste_fichier in liste_fichiers:
        liste_fichier[0] = liste_fichier[0].replace('\\', '\\\\')  # Remplacer \ par \\

    with open(nom_fichier, 'w', encoding='utf-8') as f:
        json.dump(liste_fichiers, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Veuillez spécifier le répertoire de base en argument.")
        sys.exit(1)

    repertoire_base = sys.argv[1]
    TAILLE_MINI_FICHIER_EN_MEGA_OCTET = 1
    NB_MAXI_FICHIERS = 100

    liste_fichiers = construire_liste_fichiers(repertoire_base)
    liste_triee = trier_liste_fichiers(liste_fichiers)
    gros_fichiers = filtrer_gros_fichiers(liste_triee, TAILLE_MINI_FICHIER_EN_MEGA_OCTET, NB_MAXI_FICHIERS)
    sauvegarder_json(gros_fichiers, "gros_fichiers.json")

    print(f"{len(gros_fichiers)} gros fichiers trouvés et sauvegardés dans gros_fichiers.json")
