import numpy as np

class SupplyChainTwin:
    def __init__(self, lead_time_days, daily_demand):
        self.lead_time = lead_time_days
        self.daily_demand = daily_demand
        # Stock initial : Couverture de sécurité (1.5x le lead time)
        self.initial_stock = int(lead_time_days * daily_demand * 1.5)

    def simulate_disruption(self, delay_days, duration_days):
        """
        Simule l'impact d'une rupture de flux.
        delay_days : retard de livraison.
        duration_days : durée pendant laquelle aucune commande n'arrive.
        """
        inventory_level = []
        current_stock = self.initial_stock
        
        # Simulation sur 45 jours pour voir la reprise après crise
        for day in range(1, 46):
            # Consommation constante (Sortie de stock)
            current_stock -= self.daily_demand
            
            # Logique de réapprovisionnement (Entrée de stock)
            # Si on n'est pas dans la fenêtre de "blocage" (lead_time + delay)
            if day > (self.lead_time + delay_days):
                # Le stock remonte car les livraisons reprennent
                current_stock += self.daily_demand * 1.2 # Rattrapage progressif
            
            # Sécurité : le stock ne peut pas être négatif physiquement
            inventory_level.append(max(0, current_stock))
            
        return inventory_level

if __name__ == "__main__":
    twin = SupplyChainTwin(lead_time_days=10, daily_demand=50)
    # Simulation d'un incident majeur (ex: blocage mer Rouge)
    result = twin.simulate_disruption(delay_days=10, duration_days=10)
    print(f"Simulation terminée. Stock minimum atteint : {min(result)} unités.")
            
