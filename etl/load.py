from pathlib import Path
import sqlite3
import pandas as pd

def main():
    """Charger les données transformées dans une base de données SQLite."""
    csv_path = Path("data/processed/titanic_transformed.csv")
    db_path = Path("db/titanic.db")

    if not csv_path.exists():
        raise FileNotFoundError(f"Le fichier {csv_path} n'existe pas.")

    df = pd.read_csv(csv_path)

    # Connexion à la base de données SQLite (création si elle n'existe pas)
    conn = sqlite3.connect(db_path)

    # Charger les données dans une table nommée "titanic"
    df.to_sql("titanic", conn, if_exists="replace", index=False)

    conn.close()
    print(f"Données chargées dans la base de données : {db_path.resolve()}")

if __name__ == "__main__":
    main()