age = int(input("Entrez lage : "))
sexe = input("Entrez le sexe M ou F : ")

if sexe == "M" and age > 20:
    print("impot a payer")
elif sexe == "F" and 18 <= age <= 35:
    print("impot a payer")
else:
    print("pas dimpot a payer")
