import csv

# Ecrivez le code ci-dessous. Utilisez le package csv !
# On crée une liste pour les en-têtes
en_tete = ["nom", "salaire"]
noms = []
heures_travaillees = []

with open("input.csv", encoding='utf-8') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=",")
    for ligne in reader:
        noms.append(ligne['nom'])
        heures_travaillees.append(ligne['heures_travaillees'])

try:
    # On crée un nouveau fichier pour écrire à l'intérieur
    with open("output.csv", "w", newline='') as fichier_csv:
        # On crée un objet writer avec ce fichier
        writer = csv.writer(fichier_csv, delimiter=",")
        writer.writerow(en_tete)

        # On parcourt les noms et les heures travaillées - zip permet d'itérer sur deux listes ou plus à la fois
        for nom, heure_travaillee in zip(noms, heures_travaillees):
            # On crée une nouvelle ligne avec le nom et le salaire
            salaire = int(heure_travaillee) * 15
            ligne = [nom, salaire]
            writer.writerow(ligne)
except PermissionError:
    print("Veuillez fermer le fichier data.csv.")
