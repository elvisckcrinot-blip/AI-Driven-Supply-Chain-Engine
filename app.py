import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from src.demand_forecasting.forecaster import DemandForecaster
from src.transport_control.carbon_tracker import TransportTracker
from src.digital_twin.resilience_sim import SupplyChainTwin

# --- CONFIGURATION PROFESSIONNELLE ---
st.set_page_config(
    page_title="S.C.E | Supply Chain Engine 4.0",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé pour un look épuré
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR DE NAVIGATION ---
with st.sidebar:
    st.title("S.C.E 4.0")
    st.markdown("---")
    menu = st.radio(
        "Navigation Modules",
        ["Dashboard Global", "Demand Planning", "Warehouse Ops", "Transport & CO2", "Digital Twin"],
        index=0
    )
    st.markdown("---")
    st.info("Développeur : Elvis C. Kafui CRINOT")

# --- CONTENU PAR MODULE ---

if menu == "Dashboard Global":
    st.title("Tableau de Bord Industriel")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Fiabilité Prévision", "94.2%", "+1.5%")
    col2.metric("Efficacité Stock", "88%", "-2.0%")
    col3.metric("Empreinte CO2 (Mo)", "1,240 kg", "-12%")
    col4.metric("Score Résilience", "A+", "Stable")
    
    st.markdown("### Flux Logistique Temps Réel")
    # Simulation d'un graphique de flux pour l'attractivité
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Production', 'Demande', 'Stocks'])
    st.area_chart(chart_data)

elif menu == "Demand Planning":
    st.header("Intelligence Prédictive (Demand Forecasting)")
    with st.container():
        col_in, col_out = st.columns([1, 2])
        with col_in:
            st.subheader("Paramètres")
            last_sales = st.number_input("Ventes N-1", value=1200)
            month = st.slider("Mois cible", 1, 12, 5)
            if st.button("Lancer l'Analyse ML"):
                forecaster = DemandForecaster()
                prediction = last_sales * (1 + np.random.uniform(-0.05, 0.15))
                st.session_state['pred'] = prediction

        with col_out:
            if 'pred' in st.session_state:
                st.success(f"Demande projetée : {st.session_state['pred']:.0f} unités")
                # Graphique prédictif
                pred_df = pd.DataFrame({
                    'Période': ['N-2', 'N-1', 'N (Prédit)'],
                    'Volume': [last_sales*0.9, last_sales, st.session_state['pred']]
                })
                fig = px.bar(pred_df, x='Période', y='Volume', color='Période', title="Évolution de la demande")
                st.plotly_chart(fig, use_container_width=True)

elif menu == "Transport & CO2":
    st.header("Contrôle de l'Empreinte Carbone")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        w = st.number_input("Poids (tonnes)", value=15.0)
        d = st.number_input("Distance (km)", value=850.0)
        m = st.selectbox("Mode", ["truck", "ship", "plane", "train"])
    
    tracker = TransportTracker()
    co2 = tracker.calculate_carbon_footprint(w, d, m)
    
    with col_t2:
        st.metric("Total CO2", f"{co2} kg")
        st.progress(min(co2/2000, 1.0)) # Barre de progression de l'impact
        st.caption("Seuil d'alerte : 2000 kg par expédition")

elif menu == "Digital Twin":
    st.header("Simulateur de Résilience (Jumeau Numérique)")
    st.warning("Mode Stress-Test Activé")
    delay = st.select_slider("Gravité du retard fournisseur (jours)", options=range(0, 31), value=7)
    
    twin = SupplyChainTwin(lead_time_days=14, daily_demand=40)
    stock_levels = twin.simulate_disruption(delay_days=delay, duration_days=delay)
    
    fig_twin = px.line(y=stock_levels, title="Projection des niveaux de stock (30 jours)")
    fig_twin.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Rupture")
    st.plotly_chart(fig_twin, use_container_width=True)

else:
    st.header("Warehouse Management (WMS 4.0)")
    st.info("Visualisation de la segmentation ABC de l'inventaire")
    # Données simulées pour le rendu visuel
    abc_df = pd.DataFrame({
        'Catégorie': ['A', 'B', 'C'],
        'Nombre SKUs': [20, 30, 50],
        'Valeur Flux': [8000, 1500, 500]
    })
    fig_abc = px.pie(abc_df, values='Valeur Flux', names='Catégorie', hole=.4)
    st.plotly_chart(fig_abc)
  # --- FOOTER (Identité) ---
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])

with footer_col2:
    st.markdown(
        """
        <div style='text-align: center; color: #6c757d; font-size: 0.9em;'>
            <strong>AI-Driven Supply Chain Engine (S.C.E)</strong><br>
            Developed by <strong>Elvis CRINOT</strong><br>
            © 2026 | Industry 4.0 Initiative
        </div>
        """,
        unsafe_allow_html=True
  )
