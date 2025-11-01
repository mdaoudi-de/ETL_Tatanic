from pathlib import Path
import sqlite3
import pandas as pd



def main():
    """Exécuter les requêtes SQL définies dans le fichier sql/queries.sql sur la base de données SQLite."""
    DB_PATH = Path("db/titanic.db")
    SQL_PATH = Path("sql/queries.sql")

    if not DB_PATH.exists():
        raise FileNotFoundError(f"DB introuvable: {DB_PATH.resolve()}")
    if not SQL_PATH.exists():
        raise FileNotFoundError(f"SQL introuvable: {SQL_PATH.resolve()}")

    # Nettoyer les commentaires '--' et splitter sur ';'
    lines = [
        ln for ln in SQL_PATH.read_text(encoding="utf-8").splitlines()
        if not ln.strip().startswith("--")
    ]
    sql_text = "\n".join(lines)
    statements = [s.strip() for s in sql_text.split(";") if s.strip()]

    with sqlite3.connect(str(DB_PATH)) as conn:
        for i, stmt in enumerate(statements, 1):
            if stmt.lower().startswith("select"):
                df = pd.read_sql_query(stmt, conn)
                print(f"\n[{i}] SELECT → {len(df)} lignes")
                print(df.head(20).to_string(index=False))
            else:
                conn.execute(stmt)
                print(f"\n[{i}] OK (commande exécutée)")
        conn.commit()

if __name__ == "__main__":
    main()
