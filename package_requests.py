import requests
from bs4 import BeautifulSoup
import csv

def afficherListItem(baliseOfItem, classOfItem, nomOfItem):
    print("##################### ", nomOfItem, " #####################")

    items = soup.find_all(baliseOfItem, class_=classOfItem)

    for i, item in enumerate(items):
        print(i, "-", item.string)


url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

afficherListItem("a", "gem-c-document-list__item-title", "TITRES")
afficherListItem("p", "gem-c-document-list__item-description", "DESCRIPTIONS")


titres = soup.find_all("a", class_="gem-c-document-list__item-title")
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")

# On crée une liste pour les en-têtes
en_tete = ["titre", "description"]

try:
    # On crée un nouveau fichier pour écrire à l'intérieur
    with open("data.csv", "w", newline='') as fichier_csv:
        # On crée un objet writer avec ce fichier
        writer = csv.writer(fichier_csv, delimiter=";")
        writer.writerow(en_tete)

        # On parcourt les titres et les descriptions - zip permet d'itérer sur deux listes ou plus à la fois
        for titre, description in zip(titres, descriptions):
            # On crée une nouvelle ligne avec le titre et la description
            ligne = [titre.string, description.string]
            writer.writerow(ligne)
except PermissionError:
    print("Veuillez fermer le fichier data.csv.")