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
        """
        Nettoyage et ingénierie des caractéristiques (Features Engineering).
        Inclus : extraction temporelle et décalages (lags).
        """
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        df['month'] = df['date'].dt.month
        df['year'] = df['date'].dt.year
        # Création d'un lag pour capturer la tendance récente
        df['sales_lag_1'] = df['sales'].shift(1)
        return df.dropna()

    def train(self, training_data):
        """
        Entraînement du modèle Random Forest.
        """
        df = self.preprocess_data(training_data)
        X = df[['month', 'year', 'sales_lag_1']]
        y = df['sales']

        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X, y)
        
        # Sauvegarde automatique dans le dossier models/
        if not os.path.exists('models'):
            os.makedirs('models')
        joblib.dump(self.model, self.model_path)
        return "Model trained and saved."

    def predict_demand(self, month, year, last_sales):
        """
        Prédiction de la demande pour une période donnée.
        """
        if self.model is None:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
            else:
                raise Exception("Model not trained or found.")
        
        input_data = np.array([[month, year, last_sales]])
        prediction = self.model.predict(input_data)
        return float(prediction[0])

if __name__ == "__main__":
    # Point d'entrée pour les tests unitaires locaux
    print("Demand Forecasting Module Initialized.")
      
