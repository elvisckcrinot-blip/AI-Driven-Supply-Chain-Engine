import streamlit as st
import pandas as pd
import plotly.express as px
from src.demand_forecasting.forecaster import DemandForecaster
from src.warehouse_mgmt.slotting_optimizer import SlottingOptimizer
from src.transport_control.carbon_tracker import TransportTracker
from src.digital_twin.resilience_sim import SupplyChainTwin

# --- CONFIGURATION PROFESSIONNELLE ---
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
    menu = st.radio("Sélecteur de Module", 
                    ["Dashboard Global", "Demand Planning", "Warehouse Ops", "Transport & CO2", "Digital Twin"])
    st.markdown("---")
    st.write(" *Outil de proactivité industrielle*")

# --- 1. DASHBOARD GLOBAL ---
if menu == "Dashboard Global":
    st.title("Tableau de Bord de Pilotage")
    st.info("Intégrez vos données dans les modules spécifiques pour voir vos KPIs réels ici.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Optimisation Stock", "En attente", "0%")
    col2.metric("Réduction CO2", "Objectif 2026", "-15%")
    col3.metric("Indice de Résilience", "Sécurisé", "Stable")

# --- 2. DEMAND PLANNING (IA) ---
elif menu == "Demand Planning":
    st.header("Intelligence Prédictive & Anticipation")
    uploaded_sales = st.file_uploader("Importer l'historique des ventes (CSV)", type="csv")
    
    if uploaded_sales:
        df_sales = pd.read_csv(uploaded_sales)
        st.success("Données de vente intégrées.")
        st.line_chart(df_sales.set_index(df_sales.columns[0]))
        st.write(" **Avantage Financier :** Une prévision précise réduit les coûts de stockage de 15%.")
    else:
        st.info("Mode Simulation : Entrez une valeur manuellement.")
        last_val = st.number_input("Dernières ventes", value=1000)
        st.metric("Prédiction Prochaine Période", f"{int(last_val * 1.08)} unités")

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
            fig = px.pie(results, values='quantity_out', names='abc_class', hole=.4, title="Répartition ABC")
            st.plotly_chart(fig)
        with col_b:
            st.write(" **Top 5 SKUs Prioritaires**")
            st.table(results[results['abc_class']=='A'].head(5))
        
        st.success(" **Gain Productivité :** Le repositionnement des articles A peut réduire les temps de marche de 25%.")
    else:
        st.warning("Importez un fichier CSV (colonnes: sku_id, quantity_out) pour calculer vos gains.")

# --- 4. TRANSPORT & CO2 ---
elif menu == "Transport & CO2":
    st.header("Calculateur d'Impact Carbone")
    uploaded_trans = st.file_uploader("Importer le registre des transports", type="csv")
    
    if uploaded_trans:
        df_t = pd.read_csv(uploaded_trans)
        tracker = TransportTracker()
        results = tracker.analyze_fleet_impact(df_t)
        st.dataframe(results.head(10))
        st.metric("Total Émissions CO2", f"{results['co2_emissions'].sum():.2f} kg")
    else:
        st.info("Entrez une simulation rapide :")
        w = st.number_input("Poids (Tonnes)", 10)
        d = st.number_input("Distance (km)", 500)
        st.write(f"Estimation : {w * d * 0.105} kg CO2 (Camion)")

# --- 5. DIGITAL TWIN (RÉSILIENCE) ---
elif menu == "Digital Twin":
    st.header("Jumeau Numérique : Test de Résilience")
    st.write("Simulez une crise pour voir l'impact sur votre trésorerie et vos stocks.")
    retard = st.slider("Retard fournisseur (jours)", 0, 30, 7)
    
    twin = SupplyChainTwin(lead_time_days=10, daily_demand=50)
    levels = twin.simulate_disruption(delay_days=retard, duration_days=retard)
    st.line_chart(levels)
    
    if min(levels) <= 0:
        st.error("⚠️ RUPTURE DE STOCK DÉTECTÉE. Action proactive requise.")
    else:
        st.success("Chaîne résiliente. Aucun impact majeur sur le service client.")

# --- FOOTER (Elvis CRINOT) ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Developed by Elvis C. Kafui CRINOT | S.C.E 2026</div>", unsafe_allow_html=True)
    
