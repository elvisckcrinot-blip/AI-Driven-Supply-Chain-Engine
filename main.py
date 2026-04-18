import sys
import os
import pandas as pd

# Ajout du chemin src pour permettre les imports locaux
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from demand_forecasting.forecaster import DemandForecaster
except ImportError:
    from src.demand_forecasting.forecaster import DemandForecaster

def run_forecasting_demo():
    # 1. Initialisation de l'IA
    forecaster = DemandForecaster()

    # 2. Chargement des donnees de test creees precedemment
    file_path = 'data/sales_history.csv'
    
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier {file_path} est introuvable dans le dossier data.")
        print("Assurez-vous d'avoir cree les templates CSV sur GitHub.")
        return

    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return

    # 3. Entrainement du modele (Cerveau S.C.E)
    print("--- Demarrage du S.C.E Demand Forecasting ---")
    print("Analyse des tendances historiques en cours...")
    
    status = forecaster.train(data)
    print(f"Statut : {status}")

    # 4. Simulation d une prevision pour Janvier 2026
    # On se base sur les dernieres ventes connues (ex: 200 unites en Decembre)
    prediction = forecaster.predict_demand(month=1, year=2026, last_sales=200)
    
    print("-" * 40)
    print(f"Prevision de la demande (Janvier 2026) : {prediction:.2f} unites")
    print("-" * 40)
    print("Note : Ce resultat est genere par l algorithme Random Forest.")

if __name__ == "__main__":
    run_forecasting_demo()
    
