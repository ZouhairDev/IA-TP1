nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
operateur = input("Entrez l'opérateur : ")

if operateur == "+":
    resultat = nombre1 + nombre2
    print("Le résultat est :", resultat)
elif operateur == "-":
    resultat = nombre1 - nombre2
    print("Le résultat est :", resultat)
elif operateur == "*":
    resultat = nombre1 * nombre2
    print("Le résultat est :", resultat)
elif operateur == "/":
    resultat = nombre1 / nombre2
    print("Le résultat est :", resultat)
else:
    print("Opérateur non reconnu")
