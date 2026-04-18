import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# --- FIX DEFINITIF POUR STREAMLIT CLOUD ---
# On determine la racine du projet (la ou se trouve app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# On ajoute cette racine au chemin de recherche Python
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# On ajoute aussi le dossier src au cas ou
SRC_DIR = os.path.join(BASE_DIR, 'src')
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# --- IMPORTS SECURISES ---
try:
    # Tentative d'import direct (si sys.path.insert a fonctionne)
    from demand_forecasting.forecaster import DemandForecaster
    from warehouse_mgmt.slotting_optimizer import SlottingOptimizer
    from transport_control.carbon_tracker import TransportTracker
    from digital_twin.resilience_sim import SupplyChainTwin
except ImportError:
    # Tentative d'import via le module src
    from src.demand_forecasting.forecaster import DemandForecaster
    from src.warehouse_mgmt.slotting_optimizer import SlottingOptimizer
    from src.transport_control.carbon_tracker import TransportTracker
    from src.digital_twin.resilience_sim import SupplyChainTwin

# --- CONFIGURATION DE L'INTERFACE ---
st.set_page_config(page_title="S.C.E | Industrial Intelligence", page_icon="🏗️", layout="wide")

# (Ton code d'interface continue ici...)
with st.sidebar:
    st.title("S.C.E 4.0")
    menu = st.radio("Menu", ["Dashboard Global", "Demand Planning", "Warehouse Ops", "Transport & CO2", "Digital Twin"])

if menu == "Dashboard Global":
    st.title("Tableau de Bord")
    st.info("Utilisez les modules pour voir vos indicateurs.")

elif menu == "Demand Planning":
    st.header("Intelligence Predictive")
    # Simulation simplifiee pour verifier que le module charge
    st.success("Module Demand Forecasting charge avec succes.")

elif menu == "Warehouse Ops":
    st.header("Optimisation Picking")
    st.success("Module Slotting Optimizer charge avec succes.")

elif menu == "Transport & CO2":
    st.header("Impact Carbone")
    st.success("Module Carbon Tracker charge avec succes.")

elif menu == "Digital Twin":
    st.header("Jumeau Numerique")
    st.success("Module Resilience Sim charge avec succes.")

st.markdown("---")
st.markdown("Developed by Elvis C. Kafui CRINOT")
    
