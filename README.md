# AI-Driven Supply Chain Engine (S.C.E)

Solution logicielle modulaire pilotee par l IA pour l optimisation des flux industriels, le Smart Warehousing et la resilience logistique.

---

## Architecture et Modules
Le S.C.E repose sur une architecture de micro-services Python, chacun repondant a un defi critique de la Supply Chain 4.0 :

* Demand Forecasting (IA) : Prediction de la demande via Random Forest. Anticipe les ruptures et optimise les niveaux de stock.
* WMS 4.0 (Smart Warehouse) : Optimisation du Slotting par segmentation ABC (Pareto) pour reduire les temps de picking.
* Carbon Tracker : Calculateur d empreinte CO2 multi-modal (Camion, Train, Avion, Navire) pour une logistique durable.
* Digital Twin (Jumeau Numerique) : Stress-test de la chaine logistique face aux crises (retards fournisseurs, blocages portuaires).

---

## Interface Utilisateur (Live Demo)
L application dispose d une interface Streamlit interactive permettant d importer des donnees industrielles externes.

### Procedure de test
1. Accedez a l interface via le lien de deploiement Streamlit Cloud.
2. Utilisez les fichiers modeles situes dans le dossier /data pour tester les fonctionnalites :
    * sales_history.csv : Pour la prevision de la demande.
    * inventory_data.csv : Pour l optimisation d entrepot.
    * transport_logs.csv : Pour l analyse carbone.

---

## Installation et Deploiement Local

# 1. Cloner le projet
git clone https://github.com/elvisckcrinot-blip/AI-Driven-Supply-Chain-Engine.git

# 2. Installer les dependances industrielles
pip install -r requirements.txt

# 3. Lancer le moteur
streamlit run app.py

---

## Fiabilite et Tests
Le projet inclut une suite de tests unitaires pour garantir la precision des calculs logistiques et la stabilite du code :

python -m unittest tests/test_engine.py

---

## Structure du Projet
```text
AI-Driven-SCE/
├── src/
│   ├── demand_forecasting/   # Intelligence Artificielle et Lags
│   ├── warehouse_mgmt/      # Optimisation ABC et Slotting
│   ├── transport_control/   # Calculateur CO2 GLEC
│   └── digital_twin/        # Simulation de resilience
├── models/                  # Modeles .pkl auto-geres
├── data/                    # Templates CSV (Prets a l emploi)
├── tests/                   # Validation unitaire du moteur
└── app.py                   # Interface Dashboard Industrielle

---
Développé par Elvis CRINOT | Expert en Logistique et Supply Chain 4.0
