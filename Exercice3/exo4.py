etudiants = [
    ["Alice", 20, 15.5],
    ["Bilal", 21, 14.0],
    ["Chloé", 19, 16.5],
]

print("Nom du 2e étudiant :", etudiants[1][0])
moyenne_generale = sum(etudiant[2] for etudiant in etudiants) / len(etudiants)
print("Moyenne générale :", moyenne_generale)