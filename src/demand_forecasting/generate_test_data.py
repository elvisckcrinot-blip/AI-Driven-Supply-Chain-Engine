import pandas as pd
import numpy as np
import os

def generate_industrial_dataset(output_path='data/industrial_sales_sample.csv'):
    if not os.path.exists('data'):
        os.makedirs('data')

    # Génération d'une plage de dates sur 3 ans
    dates = pd.date_range(start='2023-01-01', end='2025-12-01', freq='MS')
    n_months = len(dates)

    # Simulation de la demande : Base + Tendance + Saisonnalité + Bruit
    base_demand = 400
    trend = np.linspace(0, 200, n_months)  # Croissance de l'activité
    seasonality = 100 * np.sin(2 * np.pi * np.arange(n_months) / 12) # Cycles annuels
    noise = np.random.normal(0, 20, n_months) # Aléas logistiques

    sales = base_demand + trend + seasonality + noise
    sales = sales.clip(min=0).astype(int) # Pas de ventes négatives

    df = pd.DataFrame({'date': dates, 'sales': sales})
    df.to_csv(output_path, index=False)
    print(f"Dataset généré avec succès dans : {output_path}")

if __name__ == "__main__":
    generate_industrial_dataset()
  
