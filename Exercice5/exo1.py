def calculer_note_finale(etudiant):
    return 0.4 * etudiant["note_cc"] + 0.6 * etudiant["note_examen"]


def calculer_moyenne_classe(classe):
    if not classe:
        raise ValueError("La classe ne peut pas être vide.")
    return sum(calculer_note_finale(etudiant) for etudiant in classe) / len(classe)


def mention(note, seuil_passable=10, seuil_bien=14):
    if note < seuil_passable:
        return "AJOURNÉ"
    if note >= seuil_bien:
        return "BIEN"
    return "PASSABLE"


def statistiques(notes):
    if not notes:
        raise ValueError("La liste de notes ne peut pas être vide.")
    return sum(notes) / len(notes), min(notes), max(notes)


# Exemple DRY : le calcul et l'affichage sont définis une fois,
# puis réutilisés pour chaque étudiant.
classe = [
    {"nom": "Alice", "note_cc": 12, "note_examen": 15},
    {"nom": "Bilal", "note_cc": 14, "note_examen": 13},
    {"nom": "Chloé", "note_cc": 9, "note_examen": 16},
]


def afficher_resultat(etudiant):
    note = calculer_note_finale(etudiant)
    print(f"{etudiant['nom']} : {note:.2f} ({mention(note)})")


for etudiant in classe:
    afficher_resultat(etudiant)

print(f"Moyenne générale de la classe : {calculer_moyenne_classe(classe):.2f}")
print("Statistiques des notes d'examen :", statistiques(
    [etudiant["note_examen"] for etudiant in classe]
))