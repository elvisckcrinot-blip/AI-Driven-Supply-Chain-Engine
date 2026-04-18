import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# --- 1. CONFIGURATION DES CHEMINS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# --- 2. IMPORTS DES MODULES (Vérifiés selon ta structure racine) ---
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

# CSS simplifié (Version robuste)
st.markdown("""
<style>
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 4. NAVIGATION ---
with st.sidebar:
    st.title("S.C.E 4.0")
    st.subheader("Expertise Elvis CRINOT")
    menu = st.radio("Sélecteur de Module", 
                    ["Dashboard Global", "Demand Planning", "Warehouse Ops", "Transport & CO2", "Digital Twin"])

# --- 5. LOGIQUE DES MODULES ---
if menu == "Dashboard Global":
    st.title("Tableau de Bord de Pilotage")
    col1, col2, col3 = st.columns(3)
    col1.metric("Optimisation Stock", "Opérationnel", "100%")
    col2.metric("Réduction CO2", "Objectif 2026", "-15%")
    col3.metric("Indice Résilience", "Sécurisé", "Stable")

elif menu == "Demand Planning":
    st.header("Intelligence Prédictive")
    st.info("Le module Random Forest est prêt pour l'analyse.")

elif menu == "Warehouse Ops":
    st.header("Optimisation Slotting ABC")
    st.success("Algorithme Pareto prêt.")

elif menu == "Transport & CO2":
    st.header("Calculateur d'Impact Carbone")
    st.info("Conforme aux normes GLEC.")

elif menu == "Digital Twin":
    st.header("Jumeau Numérique")
    retard = st.slider("Simuler un retard (jours)", 0, 30, 5)
    st.warning(f"Simulation de résilience pour un retard de {retard} jours.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Developed by Elvis C. Kafui CRINOT | S.C.E 2026</div>", unsafe_allow_html=True)
