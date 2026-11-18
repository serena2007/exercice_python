class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return 0.4 * self.note_cc + 0.6 * self.note_examen

    def afficher(self):
        print(
            f"{self.nom} — contrôle continu : {self.note_cc}, "
            f"examen : {self.note_examen}"
        )


class Groupe:
    def __init__(self):
        self.etudiants = []

    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)

    def moyenne_generale(self):
        if not self.etudiants:
            raise ValueError("Le groupe ne contient aucun étudiant.")
        return sum(etudiant.moyenne() for etudiant in self.etudiants) / len(
            self.etudiants
        )


class Delegue(Etudiant):
    def __init__(self, nom, note_cc, note_examen, filiere):
        super().__init__(nom, note_cc, note_examen)
        self.filiere = filiere

    def presenter(self):
        return f"{self.nom} est délégué(e) de la filière {self.filiere}."


groupe = Groupe()
groupe.ajouter(Etudiant("Alice", 14, 16))
groupe.ajouter(Delegue("Bilal", 15, 13, "Informatique"))
groupe.ajouter(Etudiant("Chloé", 12, 18))

for etudiant in groupe.etudiants:
    etudiant.afficher()
    if isinstance(etudiant, Delegue):
        print(etudiant.presenter())

print(f"Moyenne générale du groupe : {groupe.moyenne_generale():.2f}")

meilleur_etudiant = None
for etudiant in groupe.etudiants:
    if meilleur_etudiant is None or etudiant.moyenne() > meilleur_etudiant.moyenne():
        meilleur_etudiant = etudiant

if meilleur_etudiant is not None:
    print(
        f"Meilleure moyenne : {meilleur_etudiant.nom} "
        f"({meilleur_etudiant.moyenne():.2f})"
    )