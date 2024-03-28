def est_parfait(n):
    somme = 0
    for i in range(1, n):
        if n % i == 0:
            somme += i
    return somme == n

n = int(input("Entrez un entier n : "))
if est_parfait(n):
    print(n, "est un nombre parfait.")
else:
    print(n, "n'est pas un nombre parfait.")
