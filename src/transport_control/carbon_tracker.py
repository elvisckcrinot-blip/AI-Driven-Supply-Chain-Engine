import pandas as pd

class TransportTracker:
    def __init__(self):
        # Facteurs d'émission moyens (kg CO2 par km pour 1 tonne)
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
        if mode not in self.emission_factors:
            raise ValueError("Mode de transport non supporté.")
        
        emissions = weight_tonnes * distance_km * self.emission_factors[mode]
        return round(emissions, 2)

    def analyze_fleet_impact(self, shipments_df):
        """
        Analyse l'empreinte carbone globale d'une liste d'expéditions.
        Expects columns: ['shipment_id', 'weight', 'distance', 'mode']
        """
        shipments_df['co2_emissions'] = shipments_df.apply(
            lambda x: self.calculate_carbon_footprint(x['weight'], x['distance'], x['mode']), 
            axis=1
        )
        return shipments_df

if __name__ == "__main__":
    print("Transport Control Module Initialized.")
          
