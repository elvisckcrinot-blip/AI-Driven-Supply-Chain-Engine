from src.demand_forecasting.forecaster import DemandForecaster
import pandas as pd

def run_forecasting_demo():
    # 1. Initialisation
    forecaster = DemandForecaster()

    # 2. Chargement des données générées
    try:
        data = pd.read_csv('data/industrial_sales_sample.csv')
    except FileNotFoundError:
        print("Erreur : Veuillez d'abord exécuter generate_test_data.py")
        return

    # 3. Entraînement du modèle
    print("Début de l'entraînement du cerveau S.C.E...")
    status = forecaster.train(data)
    print(status)

    # 4. Simulation d'une prévision pour Janvier 2026
    # On suppose que les dernières ventes de Décembre étaient de 650 unités
    prediction = forecaster.predict_demand(month=1, year=2026, last_sales=650)
    print(f"Prévision de la demande pour Janvier 2026 : {prediction:.2f} unités")

if __name__ == "__main__":
    run_forecasting_demo()
      
