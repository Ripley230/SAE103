# Script PowerShell pour l'analyse des gros fichiers
Write-Output "Script d'analyse des gros fichiers"

# Étape 1 : Sélection du répertoire avec le premier script Python
$rep_base = python .\script\Creation_Boutons.py
if (-not $rep_base) {
    Write-Output "Aucun répertoire sélectionné. Arrêt du script."
    exit
}

if (-not (Test-Path $rep_base)) {
    Write-Output "Le répertoire sélectionné n'existe pas. Arrêt du script."
    exit
}

# Étape 2 : Analyse des fichiers avec le second script Python
Write-Output "Analyse du répertoire : $rep_base"
python .\script\script_analyse_fichiers.py "$rep_base"

# Étape 3 : Affichage graphique des résultats
python .\script\script_affichage_graphique.py

# Vérification de la création du fichier de résultats
$fichier_resultats = "resultats_analyse.json"
if (Test-Path $fichier_resultats) {
    Write-Output "Analyse terminée avec succès."
    Write-Output "Les résultats sont disponibles dans le fichier : $fichier_resultats"
} else {
    Write-Output "Erreur : Le fichier de résultats n'a pas été créé."
}

# Attente de confirmation avant de fermer
Write-Output "`nAppuyez sur une touche pour terminer..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
