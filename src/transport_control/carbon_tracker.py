import pandas as pd

class TransportTracker:
    def __init__(self):
        # Facteurs d'émission moyens (kg CO2 par km pour 1 tonne)
        # Source standard : GLEC Framework / Base Carbone ADEME
        self.emission_factors = {
            'truck': 0.105,
            'ship': 0.012,
            'plane': 0.500,
            'train': 0.025
        }

    def calculate_carbon_footprint(self, weight_tonnes, distance_km, mode='truck'):
        """
        Calcule les émissions de CO2 pour un trajet donné.
        """
        mode = mode.lower().strip() # Nettoyage pour éviter les erreurs de casse
        if mode not in self.emission_factors:
            return 0.0 # Retourne 0 si le mode est inconnu au lieu de bloquer l'app
        
        emissions = weight_tonnes * distance_km * self.emission_factors[mode]
        return round(emissions, 2)

    def analyze_fleet_impact(self, shipments_df):
        """
        Analyse l'empreinte carbone globale d'une liste d'expéditions.
        Requiert les colonnes : ['weight', 'distance', 'mode']
        """
        # Vérification des colonnes pour éviter les crashs
        required_columns = ['weight', 'distance', 'mode']
        if not all(col in shipments_df.columns for col in required_columns):
            raise ValueError(f"Le fichier doit contenir les colonnes : {required_columns}")

        # Nettoyage rapide des données (remplacement des valeurs vides)
        df = shipments_df.copy()
        df[['weight', 'distance']] = df[['weight', 'distance']].fillna(0)
        
        # Calcul vectorisé (plus rapide sur de gros volumes de données)
        df['co2_emissions'] = df.apply(
            lambda x: self.calculate_carbon_footprint(x['weight'], x['distance'], x['mode']), 
            axis=1
        )
        return df

if __name__ == "__main__":
    # Petit test de validation
    tracker = TransportTracker()
    test_val = tracker.calculate_carbon_footprint(10, 500, 'truck')
    print(f"Test unitaire : 10t sur 500km en camion = {test_val} kg CO2")
    print("Transport Control Module Ready for Industry.")
        
