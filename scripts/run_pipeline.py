# Exécuter le pipeline ETL complet : extraction, transformation et chargement

import subprocess

def run_step(script_path):
    """Exécuter un script Python donné."""
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erreur lors de l'exécution de {script_path}:\n{result.stderr}")
        raise RuntimeError(f"Le script {script_path} a échoué.")
    print(result.stdout)

def main():
    """Exécuter les étapes du pipeline ETL."""
    steps = [
        "etl/extract.py",
        "etl/transform.py",
        "etl/load.py"
    ]
    for step in steps:
        print(f"--- Exécution de {step} ---")
        run_step(step)
    print("Pipeline ETL terminé avec succès.")

if __name__ == "__main__":
    main()