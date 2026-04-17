import pandas as pd
import numpy as np
import os
from src.transport_control.carbon_tracker import TransportTracker

def run_transport_simulation():
    if not os.path.exists('data'):
        os.makedirs('data')

    # 1. Génération de données d'expéditions simulées
    data = {
        'shipment_id': [f'SHIP_{i:03d}' for i in range(1, 11)],
        'weight': np.random.uniform(1, 25, 10).round(2),  # Tonnes
        'distance': np.random.uniform(100, 5000, 10).round(0), # km
        'mode': ['truck', 'ship', 'truck', 'plane', 'train', 'truck', 'ship', 'plane', 'truck', 'train']
    }
    
    df_shipments = pd.DataFrame(data)
    
    # 2. Initialisation du tracker et calcul
    tracker = TransportTracker()
    results = tracker.analyze_fleet_impact(df_shipments)
    
    # 3. Export des résultats pour archivage
    results.to_csv('data/transport_emissions_report.csv', index=False)
    
    # 4. Affichage du bilan opérationnel
    total_co2 = results['co2_emissions'].sum()
    print("--- Bilan Carbone Transport ---")
    print(f"Nombre d'expéditions analysées : {len(results)}")
    print(f"Émissions totales : {total_co2:.2f} kg CO2")
    
    # Analyse par mode
    impact_by_mode = results.groupby('mode')['co2_emissions'].sum().sort_values(ascending=False)
    print("\nImpact par mode de transport (kg CO2) :")
    print(impact_by_mode)

if __name__ == "__main__":
    run_transport_simulation()
  
