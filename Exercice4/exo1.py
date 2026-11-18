notes = [8, 12, 15, 17, 10, 6]

# 1. Compter les notes supérieures ou égales à 10
nombre_reussites = 0
for note in notes:
    if note >= 10:
        nombre_reussites += 1
print("Nombre de notes supérieures ou égales à 10 :", nombre_reussites)

# 2. Afficher une appréciation pour chaque note
for note in notes:
    if note < 10:
        print("ÉCHEC")
    elif note >= 14:
        print("MENTION")
    else:
        print("PASSABLE")

# 3. Augmenter le score de 3 % chaque semaine jusqu'à dépasser 60
score = 40
semaines = 0
while score <= 60:
    score *= 1.03
    semaines += 1
print("Semaines nécessaires pour dépasser 60 points :", semaines)

# 4. Comparer les notes de contrôle continu et d'examen
notes_cc = [11, 14, 9, 16]
notes_examen = [13, 12, 10, 18]

for i in range(len(notes_cc)):
    if notes_examen[i] > notes_cc[i]:
        print("PROGRESSION")
    else:
        print("PAS DE PROGRESSION")