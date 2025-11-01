# Tests pour l'étape de chargement

import unittest
import sqlite3
from pathlib import Path
import pandas as pd


def test_load_data():
    """Vérifie que les données ont été chargées dans la base de données."""
    db_path = Path("db/titanic.db")
    assert db_path.exists(), "La base de données n'existe pas."

    conn = sqlite3.connect(db_path)
    query = "SELECT COUNT(*) FROM titanic"
    cursor = conn.cursor()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    conn.close()

    assert count > 0, "La table 'titanic' est vide dans la base de données."
    print("Test de chargement réussi : les données ont été chargées dans la base de données.")

def test_load_columns():
    """Vérifie que la table 'titanic' contient les colonnes attendues."""
    db_path = Path("db/titanic.db")
    conn = sqlite3.connect(db_path)
    query = "PRAGMA table_info(titanic)"
    cursor = conn.cursor()
    cursor.execute(query)
    columns_info = cursor.fetchall()
    conn.close()

    actual_columns = [info[1] for info in columns_info]
    expected_columns = ["Passengerid", "Age", "Fare", "Sex", "Pclass", "sibsp", "Parch", "Pclass","Embarked","Survived"]
    for col in expected_columns:
        assert col in actual_columns, f"La colonne attendue '{col}' est manquante dans la table 'titanic'."
    print("Test de chargement réussi : la table contient les colonnes attendues.")

if __name__ == "__main__":
    test_load_data()
    test_load_columns()
