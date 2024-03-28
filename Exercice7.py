n = int(input("Entrez un entier non nul : "))
resultat = sum(i**2 for i in range(1, n+1))
print("Le resultat de la somme des", n, "premiers carres est :", resultat)
