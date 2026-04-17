from src.demand_forecasting.generate_test_data import generate_industrial_dataset
from src.warehouse_mgmt.test_wms import run_wms_test
from src.transport_control.test_transport import run_transport_simulation
from src.digital_twin.test_resilience import run_resilience_test

def main():
    print("=== INITIALISATION DE LA SUITE DE TESTS S.C.E ===\n")
    
    print("[1/4] Génération des données de base...")
    generate_industrial_dataset()
    
    print("\n[2/4] Test du module WMS (ABC Optimization)...")
    run_wms_test()
    
    print("\n[3/4] Test du module Transport (Carbon Footprint)...")
    run_transport_simulation()
    
    print("\n[4/4] Test du Digital Twin (Resilience Analysis)...")
    run_resilience_test()
    
    print("\n=== VALIDATION COMPLÈTE TERMINÉE : PRÊT POUR DÉPLOIEMENT ===")

if __name__ == "__main__":
    main()
  
