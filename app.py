import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# --- 1. CONFIGURATION INDUSTRIELLE DES CHEMINS ---
# On ignore le dossier 'src' s'il pose problème et on pointe vers la racine
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# --- 2. IMPORTS DIRECTS (Plus besoin de src.XXX) ---
# Assure-toi que ces fichiers sont à la RACINE comme sur ta capture 02:42
try:
    from forecaster import DemandForecaster
    from optimizer import SlottingOptimizer
    from carbon_tracker import TransportTracker
    from resilience_sim import SupplyChainTwin
except ImportError as e:
    st.error(f"Erreur de flux logique : {e}")
    st.stop()

# --- 3. INTERFACE S.C.E ---
st.set_page_config(page_title="S.C.E | Industrial Intelligence", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("S.C.E 4.0")
    st.subheader("Pilotage Performance")
    menu = st.radio("Sélecteur de Module", 
                    ["Dashboard Global", "Demand Planning", "Warehouse Ops", "Transport & CO2", "Digital Twin"])
    st.markdown("---")
    st.write("Outil de proactivité industrielle")

# --- 4. LOGIQUE DES MODULES ---
if menu == "Dashboard Global":
    st.title("Tableau de Bord de Pilotage")
    col1, col2, col3 = st.columns(3)
    col1.metric("Optimisation Stock", "En attente", "0%")
    col2.metric("Réduction CO2", "Objectif 2026", "-15%")
    col3.metric("Indice Résilience", "Sécurisé", "Stable")

elif menu == "Demand Planning":
    st.header("Intelligence Prédictive")
    val = st.number_input("Dernières ventes", value=1000)
    st.metric("Prédiction", f"{int(val * 1.08)} unités")

elif menu == "Warehouse Ops":
    st.header("Optimisation Slotting ABC")
    uploaded = st.file_uploader("Fichier WMS (CSV)", type="csv")
    if uploaded:
        # Utilisation de l'objet importé
        opt = SlottingOptimizer()
        st.success("Module Optimizer prêt.")

elif menu == "Transport & CO2":
    st.header("Impact Carbone")
    w, d = st.number_input("Tonnes", 10), st.number_input("km", 500)
    st.write(f"CO2 estimé : {w * d * 0.105} kg")

elif menu == "Digital Twin":
    st.header("Jumeau Numérique")
    retard = st.slider("Retard (jours)", 0, 30, 7)
    twin = SupplyChainTwin(lead_time_days=10, daily_demand=50)
    st.line_chart(twin.simulate_disruption(delay_days=retard, duration_days=retard))

st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Developed by Elvis C. Kafui CRINOT | S.C.E 2026</div>", unsafe_allow_html=True)
    
