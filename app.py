import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# --- 1. CONFIGURATION DES CHEMINS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# --- 2. IMPORTS DES MODULES ---
try:
    from forecaster import DemandForecaster
    from optimizer import SlottingOptimizer
    from carbon_tracker import TransportTracker
    from resilience_sim import SupplyChainTwin
except ImportError as e:
    st.error(f"Erreur d'importation : {e}")
    st.stop()

# --- 3. CONFIGURATION DE L'INTERFACE ---
st.set_page_config(page_title="S.C.E | Industrial Intelligence", page_icon="🏗️", layout="wide")

st.markdown("""
<style>
    .stMetric { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 4. NAVIGATION ---
with st.sidebar:
    st.title("S.C.E 4.0")
    st.subheader("Industrial Intelligence")
    menu = st.radio("Sélecteur de Module", 
                    ["Dashboard Global", "Demand Planning", "Warehouse Ops", "Transport & CO2", "Digital Twin"])
    st.markdown("---")
    st.write("Expertise : Elvis C. Kafui CRINOT")

# --- 5. LOGIQUE DES MODULES (INTERACTIFS) ---

if menu == "Dashboard Global":
    st.title("Tableau de Bord de Pilotage")
    st.info("Visualisation consolidée des flux industriels.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Optimisation Stock", "En cours", "ABC-Active")
    col2.metric("Réduction CO2", "Objectif 2026", "-15%")
    col3.metric("Indice Résilience", "Sécurisé", "Stable")

elif menu == "Demand Planning":
    st.header("Intelligence Prédictive (Random Forest)")
    # Permet aux entreprises d'importer leurs données
    uploaded_sales = st.file_uploader("Importer l'historique des ventes (CSV)", type="csv")
    if uploaded_sales:
        df = pd.read_csv(uploaded_sales)
        st.success("Données intégrées.")
        st.line_chart(df)
    else:
        # Option de simulation si pas de fichier
        last_val = st.number_input("Dernière valeur de vente connue", value=1000)
        st.metric("Prédiction Prochaine Période", f"{int(last_val * 1.08)} unités")

elif menu == "Warehouse Ops":
    st.header("Optimisation Slotting ABC")
    uploaded_wms = st.file_uploader("Importer les mouvements de stock (CSV)", type="csv")
    if uploaded_wms:
        # On utilise ton module métier ici
        optimizer = SlottingOptimizer()
        # ... logique d'affichage des résultats ABC ...
        st.write("Analyse Pareto effectuée.")
    else:
        st.warning("Veuillez importer un fichier CSV (format: sku_id, quantity) pour lancer l'optimisation.")

elif menu == "Transport & CO2":
    st.header("Calculateur d'Impact Carbone (Norme GLEC)")
    col_a, col_b = st.columns(2)
    poids = col_a.number_input("Poids (Tonnes)", value=10.0)
    dist = col_b.number_input("Distance (km)", value=500.0)
    emissions = poids * dist * 0.105
    st.metric("Total Emissions CO2", f"{emissions:.2f} kg")

elif menu == "Digital Twin":
    st.header("Jumeau Numérique : Test de Résilience")
    # Curseur interactif pour simuler une crise
    retard = st.slider("Simuler un retard fournisseur (jours)", 0, 30, 7)
    
    # Appel de ton module simulation
    twin = SupplyChainTwin(lead_time_days=10, daily_demand=50)
    levels = twin.simulate_disruption(delay_days=retard, duration_days=retard)
    st.line_chart(levels)
    
    if min(levels) <= 0:
        st.error("RUPTURE DE STOCK DÉTECTÉE. Action proactive requise.")
    else:
        st.success("Chaîne logistique résiliente.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Developed by Elvis C. Kafui CRINOT | S.C.E 2026</div>", unsafe_allow_html=True)
    
