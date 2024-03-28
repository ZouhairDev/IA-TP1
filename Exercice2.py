import math

a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))
c = float(input("Entrez la valeur de c : "))

delta = b**2 - 4*a*c
print("Delta = ", delta)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Les solutions sont :", x1, "et", x2)
elif delta == 0:
    x = -b / (2*a)
    print("La solution double est :", x)
else:
    print("Pas de solution reelle")
