def decomposer_en_premiers(nombre):
    facteurs_premiers = []
    diviseur = 2

    while nombre > 1:
        while nombre % diviseur == 0:
            facteurs_premiers.append(diviseur)
            nombre //= diviseur
        diviseur += 1

    return facteurs_premiers

# Demander à l'utilisateur d'entrer un nombre
nombre_entre = int(input("Entrez un nombre entier positif : "))

# Vérifier si le nombre est valide
if nombre_entre <= 0:
    print("Veuillez entrer un nombre entier positif.")
else:
    # Appeler la fonction pour décomposer en facteurs premiers
    resultats = decomposer_en_premiers(nombre_entre)
    
    # Afficher le résultat
    print(f"Les facteurs premiers de {nombre_entre} sont : {resultats}")
