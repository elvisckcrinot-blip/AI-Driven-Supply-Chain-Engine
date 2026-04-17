import matplotlib.pyplot as plt
import os
from src.digital_twin.resilience_sim import SupplyChainTwin

def run_resilience_test():
    # 1. Configuration du Jumeau Numérique
    # Délai : 10 jours | Demande : 50 unités/jour
    twin = SupplyChainTwin(lead_time_days=10, daily_demand=50)

    # 2. Scénario A : Flux normal (Pas de retard)
    normal_flow = twin.simulate_disruption(delay_days=0, duration_days=0)

    # 3. Scénario B : Crise Logistique (Retard de 7 jours)
    crisis_flow = twin.simulate_disruption(delay_days=7, duration_days=7)

    # 4. Analyse des résultats
    print("--- Rapport de Résilience S.C.E ---")
    print(f"Stock minimum en flux normal : {min(normal_flow)} unités")
    print(f"Stock minimum en temps de crise : {min(crisis_flow)} unités")

    if min(crisis_flow) <= 0:
        print("\nALERTE CRITIQUE : Le modèle prédit une rupture de stock.")
        print("Action suggérée : Augmenter le stock de sécurité ou diversifier les sources.")
    else:
        print("\nSUCCÈS : La chaîne est résiliente face à ce scénario.")

    # Optionnel : Sauvegarde des résultats
    if not os.path.exists('data'):
        os.makedirs('data')
    
    print("\nSimulation terminée. Données prêtes pour analyse comparative.")

if __name__ == "__main__":
    run_resilience_test()
  
