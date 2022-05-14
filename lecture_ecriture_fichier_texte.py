fichier = open("hello.txt", "w")
fichier.write("Hello world !")
fichier.close()

with open("hello.txt") as fichier:
    for ligne in fichier:
        print(ligne)