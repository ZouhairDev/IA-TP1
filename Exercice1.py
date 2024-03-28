note1 = float(input("Entrez la premiere note : "))
note2 = float(input("Entrez la deuxieme note : "))
note3 = float(input("Entrez la troisieme note : "))

moyenne = (note1 + note2 + note3) / 3

print("La moyenne est :", moyenne)

if moyenne >= 16:
    print("Tres bien")
elif 14 <= moyenne < 16:
    print("Bien")
elif 12 <= moyenne < 14:
    print("Assez bien")
elif 10 <= moyenne < 12:
    print("Passable")
else:
    print("Insuffisant")
