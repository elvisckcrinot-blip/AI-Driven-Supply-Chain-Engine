import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# --- DETECTION DYNAMIQUE DU CHEMIN RACINE ---
# Cette ligne permet de trouver le dossier parent de 'src' et de l'ajouter au système
root_path = os.path.dirname(os.path.abspath(__file__))
if root_path not in sys.path:
    sys.path.append(root_path)

# On ajoute aussi explicitement le dossier 'src'
src_path = os.path.join(root_path, 'src')
if src_path not in sys.path:
    sys.path.append(src_path)

# --- IMPORTS DES MODULES LOCAUX (SYNTAXE ROBUSTE) ---
try:
    from src.demand_forecasting.forecaster import DemandForecaster
    from src.warehouse_mgmt.slotting_optimizer import SlottingOptimizer
    from src.transport_control.carbon_tracker import TransportTracker
    from src.digital_twin.resilience_sim import SupplyChainTwin
except ImportError:
    # Backup si le sys.path a déjà fait le travail pour le dossier src
    from demand_forecasting.forecaster import DemandForecaster
    from warehouse_mgmt.slotting_optimizer import SlottingOptimizer
    from transport_control.carbon_tracker import TransportTracker
    from digital_twin.resilience_sim import SupplyChainTwin

# --- CONFIGURATION ---
st.set_page_config(page_title="S.C.E | Industrial Intelligence", page_icon="🏗️", layout="wide")

# (Le reste du code de ton interface reste identique)
# --- SIDEBAR ---
with st.sidebar:
    st.title("S.C.E 4.0")
    st.subheader("Pilotage de la Performance")
    menu = st.radio("Selecteur de Module", 
                    ["Dashboard Global", "Demand Planning", "Warehouse Ops", "Transport & CO2", "Digital Twin"])

# --- 1. DASHBOARD GLOBAL ---
if menu == "Dashboard Global":
    st.title("Tableau de Bord de Pilotage")
    st.info("Integrez vos donnees dans les modules specifiques pour voir vos KPIs reels ici.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Optimisation Stock", "En attente", "0%")
    col2.metric("Reduction CO2", "Objectif 2026", "-15%")
    col3.metric("Indice de Resilience", "Securise", "Stable")

# --- 2. DEMAND PLANNING (IA) ---
elif menu == "Demand Planning":
    st.header("Intelligence Predictive & Anticipation")
    uploaded_sales = st.file_uploader("Importer l'historique des ventes (CSV)", type="csv")
    if uploaded_sales:
        df_sales = pd.read_csv(uploaded_sales)
        st.success("Donnees de vente integrees.")
        st.line_chart(df_sales.set_index(df_sales.columns[0]))
    else:
        st.info("Prevision basee sur le dernier historique connu.")
        st.metric("Prediction Prochaine Periode", "En attente de donnees")

# --- 3. WAREHOUSE OPS (SLOTTING) ---
elif menu == "Warehouse Ops":
    st.header("Optimisation du Picking (Slotting ABC)")
    uploaded_wms = st.file_uploader("Importer les mouvements de stock (CSV)", type="csv")
    if uploaded_wms:
        optimizer = SlottingOptimizer()
        df_wms = pd.read_csv(uploaded_wms)
        optimizer.data = df_wms
        results = optimizer.calculate_abc_segmentation()
        fig = px.pie(results, values='quantity_out', names='abc_class', hole=.4, title="Repartition ABC")
        st.plotly_chart(fig)
    else:
        st.warning("Importez un fichier CSV (sku_id, quantity_out).")

# --- 4. TRANSPORT & CO2 ---
elif menu == "Transport & CO2":
    st.header("Calculateur d'Impact Carbone")
    w = st.number_input("Poids (Tonnes)", 10)
    d = st.number_input("Distance (km)", 500)
    st.write(f"Estimation : {w * d * 0.105} kg CO2 (Camion)")

# --- 5. DIGITAL TWIN (RESILIENCE) ---
elif menu == "Digital Twin":
    st.header("Jumeau Numerique : Test de Resilience")
    retard = st.slider("Retard fournisseur (jours)", 0, 30, 7)
    twin = SupplyChainTwin(lead_time_days=10, daily_demand=50)
    levels = twin.simulate_disruption(delay_days=retard, duration_days=retard)
    st.line_chart(levels)

st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Developed by Elvis C. Kafui CRINOT | S.C.E 2026</div>", unsafe_allow_html=True)
    
