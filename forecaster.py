import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

class DemandForecaster:
    def __init__(self, model_path='models/demand_rf_model.pkl'):
        self.model_path = model_path
        self.model = None

    def preprocess_data(self, df):
        """Nettoyage et engineering : mois, année et lag de vente."""
        # Sécurité pour les données d'entrée
        df = df.copy()
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        df['month'] = df['date'].dt.month
        df['year'] = df['date'].dt.year
        df['sales_lag_1'] = df['sales'].shift(1)
        return df.dropna()

    def train(self, training_data):
        """Entraînement et sauvegarde du Random Forest."""
        df = self.preprocess_data(training_data)
        X = df[['month', 'year', 'sales_lag_1']]
        y = df['sales']

        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X, y)
        
        if not os.path.exists('models'):
            os.makedirs('models')
        joblib.dump(self.model, self.model_path)
        return "Model trained and saved."

    def load_model(self):
        """Charge le modèle ou déclenche un entraînement par défaut si absent."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            # Sécurité industrielle : Si pas de modèle, on en crée un petit 
            # avec des données fictives pour ne pas bloquer l'interface.
            print("Modèle absent. Entraînement d'un modèle de secours...")
            data = {
                'date': pd.date_range(start='2024-01-01', periods=12, freq='ME'),
                'sales': [100, 120, 110, 130, 150, 140, 160, 180, 170, 190, 210, 200]
            }
            self.train(pd.DataFrame(data))

    def predict_demand(self, month, year, last_sales):
        """Prédiction robuste."""
        if self.model is None:
            self.load_model()
        
        input_data = np.array([[month, year, last_sales]])
        prediction = self.model.predict(input_data)
        return float(prediction[0])

if __name__ == "__main__":
    print("Demand Forecasting Module (AI 4.0) Ready.")
            
