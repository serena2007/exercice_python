import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# 1–2. Notes par évaluation et moyenne glissante sur trois évaluations
evaluations = [
    "Quiz 1", "Devoir 1", "Quiz 2", "Devoir 2", "Quiz 3",
    "Devoir 3", "Quiz 4", "Devoir 4", "Quiz 5", "Examen",
]
notes = [11, 13, 12, 15, 14, 16, 13, 17, 15, 18]

moyenne_glissante = [
    sum(notes[i - 2:i + 1]) / 3
    for i in range(2, len(notes))
]

plt.figure(figsize=(10, 5))
plt.plot(evaluations, notes, marker="o", label="Notes")
plt.plot(
    evaluations[2:],
    moyenne_glissante,
    marker="s",
    label="Moyenne glissante (3 évaluations)",
)
plt.title("Notes et moyenne glissante par évaluation")
plt.xlabel("Évaluation")
plt.ylabel("Note")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()


# 3. Nombre d'étudiants par filière
filieres = ["Informatique", "Mathématiques", "Physique", "Biologie"]
effectifs = [32, 24, 18, 21]

plt.figure(figsize=(8, 5))
plt.bar(filieres, effectifs)
plt.title("Nombre d'étudiants par filière")
plt.xlabel("Filière")
plt.ylabel("Nombre d'étudiants")
plt.tight_layout()


# 4. Notes et taux de présence par semaine, avec un axe des semaines partagé
semaines = [1, 2, 3, 4, 5, 6]
notes_hebdomadaires = [12, 13, 11, 15, 14, 16]
taux_presence = [92, 95, 88, 97, 94, 98]

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(8, 7))
axes[0].plot(semaines, notes_hebdomadaires, marker="o")
axes[0].set_title("Notes et taux de présence par semaine")
axes[0].set_ylabel("Note")
axes[1].plot(semaines, taux_presence, marker="o", color="green")
axes[1].set_xlabel("Semaine")
axes[1].set_ylabel("Présence (%)")
fig.tight_layout()


# 5. Distribution des notes
notes_classe = [8, 10, 11, 12, 12, 13, 14, 14, 15, 16, 17, 18]

plt.figure(figsize=(8, 5))
sns.histplot(notes_classe, kde=True)
plt.title("Distribution des notes")
plt.xlabel("Note")
plt.ylabel("Effectif")
plt.tight_layout()


# 6. Corrélations entre les notes de trois matières
donnees = {
    "Mathématiques": [15, 12, 17, 10, 14, 18, 11, 16, 13, 19],
    "Français": [13, 14, 15, 11, 12, 16, 10, 15, 14, 17],
    "Informatique": [17, 11, 18, 9, 15, 19, 12, 17, 13, 20],
}
df_notes = pd.DataFrame(donnees, index=[f"Étudiant {i}" for i in range(1, 11)])
matrice_correlation = df_notes.corr()

plt.figure(figsize=(7, 5))
sns.heatmap(matrice_correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Corrélation entre les notes des matières")
plt.tight_layout()

plt.show()