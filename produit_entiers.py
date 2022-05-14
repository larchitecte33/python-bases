# Vous allez créer une fonction permettant de calculer le produit d'une liste de nombres

# Ecrivez la fonction et testez avec le bouton > "Run" que le calcul est correct !
def produit_entiers(liste_entiers):
    # écrivez le code ici
    if len(liste_entiers) == 0:
        return 0
    else:
        resultat = 1

        for nombre in liste_entiers:
            resultat = resultat * nombre

        return resultat

# Ne touchez pas le code de vérification ci-dessous :)
assert 1 == produit_entiers([1, 1, 1])
assert 6 == produit_entiers([1, 2, 3])
assert 0 == produit_entiers([1, 2, 3, 90, 0])
