# Tests pour l'étape de transformation

from pathlib import Path
import pandas as pd

def test_transformation_data():
    """Vérifie que le fichier transformé existe et contient des données."""
    transformed_path = Path("data/processed/titanic_transformed.csv")
    assert transformed_path.exists(), "Le fichier transformé n'existe pas."

    df = pd.read_csv(transformed_path)
    assert not df.empty, "Le fichier transformé est vide."
    print("Test de transformation réussi : le fichier existe et contient des données.")

def test_transformation_columns():
    """Vérifie que le fichier transformé contient les colonnes attendues."""
    transformed_path = Path("data/processed/titanic_transformed.csv")
    df = pd.read_csv(transformed_path)
    expected_columns = ["Passengerid", "Age", "Fare", "Sex", "Pclass", "sibsp", "Parch", "Embarked", "Survived"]
    for col in expected_columns:
        assert col in df.columns, f"La colonne attendue '{col}' est manquante dans le fichier transformé."
    print("Test de transformation réussi : le fichier contient les colonnes attendues.")

def test_no_missing_embarked():
    """Vérifie qu'il n'y a pas de valeurs manquantes dans la colonne 'Embarked'."""
    transformed_path = Path("data/processed/titanic_transformed.csv")
    df = pd.read_csv(transformed_path)
    assert df["Embarked"].isnull().sum() == 0, "Il y a des valeurs manquantes dans la colonne 'Embarked'."
    print("Test de transformation réussi : aucune valeur manquante dans la colonne 'Embarked'.")

if __name__ == "__main__":
    test_transformation_data()
    test_transformation_columns()
    test_no_missing_embarked()