somme_notes = 187.5
nombre_copies = 15
note_validation = 10

moyenne = somme_notes / nombre_copies
ecart = abs(moyenne - note_validation)

print(f"Moyenne de la classe : {moyenne}")
print(f"Écart avec la note de validation : {ecart}")