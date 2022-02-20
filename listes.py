plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
# Affiche "Facebook"
print(plateformes_sociales[0])
# Affiche "Instagram"
print(plateformes_sociales[1])
# Affiche "Twitter"
print(plateformes_sociales[-1])

langage_de_programmation = "PYTHON"
# Affiche "T"
print(langage_de_programmation[2])
# Affiche "T"
print(langage_de_programmation[-4])

plateformes_sociales.append("TikTok")
# Affiche ['Facebook', 'Instagram', 'Snapchat', 'Twitter', 'TikTok']
print(plateformes_sociales)

plateformes_sociales.remove("Snapchat")
# Affiche ['Facebook', 'Instagram', 'Twitter', 'TikTok']
print(plateformes_sociales)

# Affiche longueur de la liste = 4
print("longueur de la liste = " + str(len(plateformes_sociales)))

plateformes_sociales.sort()
# Affiche ['Facebook', 'Instagram', 'TikTok', 'Twitter']
print(plateformes_sociales)