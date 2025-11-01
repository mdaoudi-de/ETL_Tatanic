# Tests pour l'étape d'extraction

from pathlib import Path
import pandas as pd

def test_extraction_data():
    """Vérifie que le fichier extrait existe et contient des données."""
    extracted_path = Path("data/staging/titanic_extracted.csv")
    assert extracted_path.exists(), "Le fichier extrait n'existe pas."

    df = pd.read_csv(extracted_path)
    assert not df.empty, "Le fichier extrait est vide."
    print("Test d'extraction réussi : le fichier existe et contient des données.")


def test_extraction_columns():
    """Vérifie que le fichier extrait contient les colonnes attendues."""
    extracted_path = Path("data/staging/titanic_extracted.csv")
    df = pd.read_csv(extracted_path)
    expected_columns = ["Passengerid", "Age", "Fare", "Sex", "Pclass", "sibsp", "Parch", "Pclass","Embarked","2urvived"]
    for col in expected_columns:
        assert col in df.columns, f"La colonne attendue '{col}' est manquante dans le fichier extrait."
    print("Test d'extraction réussi : le fichier contient les colonnes attendues.")


if __name__ == "__main__":
    test_extraction_data()
    test_extraction_columns()
