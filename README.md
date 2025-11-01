# ETL Titanic — CSV → SQLite

Mini-pipeline **ETL** (Extraction–Transformation–Chargement) qui lit un CSV *Titanic*, applique un nettoyage léger puis charge le résultat dans une base **SQLite**. Le projet est pensé pour être simple à cloner, exécuter et tester (local + Docker).

---

## Sommaire
- [Aperçu](#aperçu)
- [Architecture du dépôt](#architecture-du-dépôt)
- [Prérequis](#prérequis)
- [Installation (local)](#installation-local)
- [Données attendues](#données-attendues)
- [Exécution du pipeline](#exécution-du-pipeline)
- [Résultats & sorties](#résultats--sorties)
- [Tests](#tests)
- [Docker (build & run)](#docker-build--run)
- [Dépannage](#dépannage)
- [Licence](#licence)

---

## Aperçu

- **Extract** : copie le fichier brut `data/raw/titanic.csv` vers une zone *staging* (sans transformation).
- **Transform** : opérations de nettoyage de base (ex. gestion NA, types, colonnes utiles) pour produire un CSV *processed*.
- **Load** : chargement du jeu de données nettoyé dans **SQLite** (table dédiée) + requêtes SQL d’exemple.

> Les dossiers `data/staging` et `data/processed` sont créés au premier run si absents (ils peuvent être ignorés par Git).

---

## Architecture du dépôt

```
.
├── data/
│   ├── staging/
│   ├── processsed/
│   └── raw/     
│       └── titanic.csv            # titanic.csv (données sources)
├── etl/                           # modules ETL (extract.py, transform.py, load.py, utils, etc.)
│   ├── extract.py
│   ├── load.py
│   └── transform.py                    
├── notebooks/  
│   └── explorations.ipynb             # notebooks d’exploration
├── scripts/
│   └── run_pipeline.py      # point d’entrée : orchestre Extract -> Transform -> Load
├── sql/
│   ├── run_queries.py    
│   └── queries.sql          
├── tests/
│   ├── test_extract.py
│   ├── test_load.py
│   └── test_transform.py                   
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Prérequis

- **Python** 3.11
- `pip` / `venv`
- (Optionnel) **Docker** 24+

---

## Installation (local)

```bash
# 1) cloner
git clone https://github.com/mdaoudi-de/ETL_Tatanic.git
cd ETL_Tatanic

# 2) créer un environnement virtuel
python -m venv .venv
# Linux/Mac:
source .venv/bin/activate
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# 3) installer les dépendances
pip install -r requirements.txt
```

---

## Données attendues

Placer le fichier source **Titanic** en CSV ici :

```
data/raw/titanic.csv
```

- Encodage : `utf-8`
- Séparateur : `,`
- L’en-tête doit contenir les noms de colonnes usuels du dataset Titanic.

> Si `data/staging` et `data/processed` n’existent pas, ils seront créés automatiquement au premier run.

---

## Exécution du pipeline

Exécuter le point d’entrée :

```bash
# depuis la racine du projet
python scripts/run_pipeline.py
```

Comportement attendu (log) :
- lecture de `data/raw/titanic.csv`
- écriture en **staging**
- transformations minimales
- chargement en **SQLite** (base et table créées si besoin)

> Les chemins par défaut et le nom de la base SQLite sont définis dans le code (`etl/load.py`). Par défaut, la base est écrite sous `data/processed/`.

---

## Résultats & sorties

- **CSV staging** : `data/staging/titanic_extracted.csv`
- **CSV final** : `data/processed/titanic_clean.csv` *(nom indicatif ; voir le code si différent)*
- **Base SQLite** : `data/processed/<nom_base>.db` *(ex. `titanic.db` ; voir `etl/load.py`)*
- **SQL d’exemple** : répertoire `sql/` (création de table + requêtes analytiques)

---

## Tests

Le projet inclut des **tests unitaires** (pytest) sur les étapes clés (existence des fichiers, schéma minimal, etc.).

```bash
# exécuter tous les tests
pytest -q

# filtrer un test
pytest -q -k test_extraction_data
```

---

## Docker (build & run)

Construire l’image :

```bash
docker build -t etl-titanic .
```

Lancer le pipeline en montant le dossier `data/` pour récupérer les sorties :

**Windows PowerShell**
```powershell
docker run --rm -v "${PWD}\data:/app/data" etl-titanic
```

> Le conteneur exécute le pipeline (équivalent à `python scripts/run_pipeline.py`) et écrit les résultats dans `data/` côté hôte.

---

## Dépannage

- **Fichier introuvable** : vérifie que `data/raw/titanic.csv` existe et que son nom est exact (casse, extension).
- **Chemins Windows** : lance PowerShell en admin si besoin. Utilise `\` dans les chemins et `${PWD}` pour le bind Docker.
- **Encodage/colonnes** : assure que le CSV est en `utf-8` et séparé par des virgules. Ajuste les options `pd.read_csv` si nécessaire.
- **Dossiers manquants** : `Path(...).mkdir(parents=True, exist_ok=True)` dans le code crée `data/staging` et `data/processed` au run.

---

## Licence

MIT — faites-en bon usage.


