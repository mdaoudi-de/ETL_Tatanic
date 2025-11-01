from pathlib import Path               
import pandas as pd 

# Point d'entrée du script d'extraction
def main():
    """Extraire les données du fichier CSV brut et les enregistrer dans le répertoire staging."""
    csv_path = Path("data/raw/titanic.csv")
    out_dir = Path("data/staging")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "titanic_extracted.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Le fichier {csv_path} n'existe pas.")
    
    df = pd.read_csv(csv_path)

    df.to_csv(out_path, index=False)        
    print(f"Écrit : {out_path.resolve()}")

if __name__ == "__main__":                 
    main() 