import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# --- GESTION DES CHEMINS (Correction ModuleNotFoundError) ---
# On ajoute le dossier 'src' au chemin de recherche de Python
current_dir = os.path.dirname(__file__)
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.append(src_path)

# --- IMPORTS DES MODULES LOCAUX ---
try:
    from demand_forecasting.forecaster import DemandForecaster
    from warehouse_mgmt.slotting_optimizer import SlottingOptimizer
    from transport_control.carbon_tracker import TransportTracker
    from digital_twin.resilience_sim import SupplyChainTwin
except ImportError:
    from src.demand_forecasting.forecaster import DemandForecaster
    from src.warehouse_mgmt.slotting_optimizer import SlottingOptimizer
    from src.transport_control.carbon_tracker import TransportTracker
    from src.digital_twin.resilience_sim import SupplyChainTwin

# --- CONFIGURATION ---
st.set_page_config(page_title="S.C.E | Industrial Intelligence", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("S.C.E 4.0")
    st.subheader("Pilotage de la Performance")
    menu = st.radio("Selecteur de Module", 
                    ["Dashboard Global", "Demand Planning", "Warehouse Ops", "Transport & CO2", "Digital Twin"])
    st.markdown("---")
    st.write("Outil de proactivite industrielle")

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
        st.info("Mode Simulation : Entrez une valeur manuellement.")
        last_val = st.number_input("Dernieres ventes", value=1000)
        st.metric("Prediction Prochaine Periode", f"{int(last_val * 1.08)} unites")

# --- 3. WAREHOUSE OPS (SLOTTING) ---
elif menu == "Warehouse Ops":
    st.header("Optimisation du Picking (Slotting ABC)")
    uploaded_wms = st.file_uploader("Importer les mouvements de stock (CSV)", type="csv")
    
    if uploaded_wms:
        optimizer = SlottingOptimizer()
        df_wms = pd.read_csv(uploaded_wms)
        optimizer.data = df_wms
        results = optimizer.calculate_abc_segmentation()
        
        col_a, col_b = st.columns(2)
        with col_a:
            fig = px.pie(results, values='quantity_out', names='abc_class', hole=.4, title="Repartition ABC")
            st.plotly_chart(fig)
        with col_b:
            st.write("Top 5 SKUs Prioritaires")
            st.table(results[results['abc_class']=='A'].head(5))
    else:
        st.warning("Importez un fichier CSV (sku_id, quantity_out) pour calculer vos gains.")

# --- 4. TRANSPORT & CO2 ---
elif menu == "Transport & CO2":
    st.header("Calculateur d'Impact Carbone")
    uploaded_trans = st.file_uploader("Importer le registre des transports", type="csv")
    
    if uploaded_trans:
        df_t = pd.read_csv(uploaded_trans)
        tracker = TransportTracker()
        results = tracker.analyze_fleet_impact(df_t)
        st.dataframe(results.head(10))
        st.metric("Total Emissions CO2", f"{results['co2_emissions'].sum():.2f} kg")
    else:
        st.info("Entrez une simulation rapide :")
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
    
    if min(levels) <= 0:
        st.error("RUPTURE DE STOCK DETECTEE. Action proactive requise.")
    else:
        st.success("Chaine resiliente.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Developed by Elvis C. Kafui CRINOT | S.C.E 2026</div>", unsafe_allow_html=True)
    
