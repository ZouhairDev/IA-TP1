Temps = int(input("Entrez le temps en secondes : "))

heures = Temps // 3600
Temps %= 3600
minutes = Temps // 60
secondes = Temps % 60

print(Temps, "seconds =", heures, "heures", minutes, "minutes", secondes, "secondes")
