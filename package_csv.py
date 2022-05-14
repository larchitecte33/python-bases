import csv23
import csv

with csv23.open_reader("couleurs_preferees.csv", delimiter=';') as csvreader:
    for ligne in csvreader:
        print(ligne)


with open("couleurs_preferees.csv", encoding='utf-8') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=";")
    for ligne in reader:
      print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])