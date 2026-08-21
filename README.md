# AlexandrIcam

Plateforme (site statique, sans backend) de partage de ressources pédagogiques entre étudiants de l'ICAM Toulouse (apprentissage) : cours, sujets d'examens, conseils stage/alternance, recettes de cuisine étudiante, et quelques mini-jeux pour la pause.

Reprise/nettoyage du projet [AlexandrIcam](https://github.com/KoroKira/AlexandrIcam) original.

## Pages

- `cours.html` — banque de cours filtrable par année/matière/type, alimentée par `cours/cours.json`
- `exams.html` — banque d'annales (actuellement données d'exemple seulement, pas de vraies annales chargées)
- `stage.html` — ressources CV/lettre de motivation et liste d'entreprises partenaires
- `cuisine.html` — recettes étudiantes, alimentées par `cuisine/recettes.json`
- `user.html` — raccourcis vers les mini-jeux (Démineur, Sudoku, Tetris, Échecs), page purement statique (pas de compte utilisateur réel)

## Fonctionnement

Site 100% statique (HTML/CSS/JS vanilla), sans build ni backend : chaque page charge un fichier JSON (`cours/cours.json`, `exams/exams.json`, `cuisine/recettes.json`) qui référence des fichiers stockés dans `uploads/`.

## Lancer en local

```bash
python3 -m http.server 8000
```

Puis ouvrir `http://localhost:8000`.

## État du projet / ce qu'il reste à faire

- **Banque de cours** : ~200 fichiers référencés sur les 305 uploadés (A1/A2). Les années A3-A5 n'ont que des pages vides (`info.html`, `physique.html`, `maths.html` sans contenu).
- **`uploads/annee/meca`** contient une centaine de fichiers de mécanique jamais rattachés à une année/matière dans le catalogue — à trier.
- **Annales (`exams.html`)** : encore des données d'exemple, aucune vraie annale chargée.
- **Poids du repo** : ~400 Mo de PDF versionnés directement dans git (pas de Git LFS) — à surveiller si le volume continue de grossir.
- Les rapports de stage nominatifs d'autres étudiants ont été retirés du dépôt (y compris de l'historique) pour des raisons de confidentialité — seuls des documents génériques (méthode CV/LM, liste d'entreprises) sont conservés.
