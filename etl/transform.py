from pathlib import Path
import pandas as pd


# Point d'entrée du script de transformation
def main():
    """Transformer les données extraites et les enregistrer dans le répertoire processed."""
    csv_path = Path("data/staging/titanic_extracted.csv")
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "titanic_transformed.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Le fichier {csv_path} n'existe pas.")

    df = pd.read_csv(csv_path)

    df = df[["Passengerid", "Age", "Fare", "Sex", "Pclass", "sibsp", "Parch", "Pclass","Embarked","2urvived"]]

    # Renommer la colonne "2urvived" en "Survived"
    df = df.rename(columns={"2urvived": "Survived"})

    # Suppression des lignes avec des valeurs manquantes dans la colonne "Embarked"
    df = df.dropna(subset=["Embarked"])


    df.to_csv(out_path, index=False)
    print(f"Écrit : {out_path.resolve()}")

if __name__ == "__main__":
    main()