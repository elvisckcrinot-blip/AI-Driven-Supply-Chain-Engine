import numpy as np

class SupplyChainTwin:
    def __init__(self, lead_time_days, daily_demand):
        self.lead_time = lead_time_days
        self.daily_demand = daily_demand
        self.stock = lead_time_days * daily_demand # Stock de sécurité théorique

    def simulate_disruption(self, delay_days, duration_days):
        """
        Simule l'impact d'un retard fournisseur.
        delay_days : nombre de jours de retard ajoutés au délai habituel.
        duration_days : combien de temps dure la crise.
        """
        inventory_level = []
        current_stock = self.stock
        
        # Simulation sur 30 jours
        for day in range(1, 31):
            # Consommation quotidienne
            current_stock -= self.daily_demand
            
            # Réapprovisionnement avec retard
            if day == (self.lead_time + delay_days):
                current_stock += (self.lead_time * self.daily_demand)
            
            inventory_level.append(max(0, current_stock))
            
        return inventory_level

if __name__ == "__main__":
    # Test rapide du jumeau numérique
    twin = SupplyChainTwin(lead_time_days=10, daily_demand=50)
    # On simule un blocage portuaire de 5 jours
    result = twin.simulate_disruption(delay_days=5, duration_days=5)
    print(f"Niveaux de stock simulés sur 30 jours : {result}")
    if 0 in result:
        print("ALERTE : Rupture de stock détectée pendant la simulation.")
      
