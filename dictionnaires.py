nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne nous aimons les chiens",
    "date_de_début": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

# Affiche "Jeanne d'Arc"
print(nouvelle_campagne['responsable_de_campagne'])

# Affiche "3.4"
print(taux_de_conversion['facebook'])


infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"

# Affiche {'poids': '13 à 16 kg', 'origine': 'États-Unis', 'nom_scientifique': 'Canis lupus familiaris'}
print(infos_labradoodle)

del(infos_labradoodle['origine'])

# Affiche {'poids': '13 à 16 kg', 'nom_scientifique': 'Canis lupus familiaris'}
print(infos_labradoodle)

# Affiche True
print("poids" in infos_labradoodle)
# Affiche False
print("race" in infos_labradoodle)