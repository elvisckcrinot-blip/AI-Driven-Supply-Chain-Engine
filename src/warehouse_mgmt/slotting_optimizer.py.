import pandas as pd

class SlottingOptimizer:
    def __init__(self):
        self.data = None

    def load_inventory_data(self, data_source):
        """
        Charge les données depuis un chemin (string) ou un objet fichier (Streamlit).
        """
        if isinstance(data_source, str):
            self.data = pd.read_csv(data_source)
        else:
            # Pour Streamlit : lit directement l'objet UploadedFile
            self.data = pd.read_csv(data_source)

    def calculate_abc_segmentation(self):
        """
        Analyse ABC basée sur la fréquence de sortie (Pareto 80/20).
        """
        if self.data is None or self.data.empty:
            return pd.DataFrame()

        # Nettoyage minimal pour éviter les crashs avec des données réelles
        df = self.data.copy()
        if 'sku_id' not in df.columns or 'quantity_out' not in df.columns:
            raise ValueError("Le fichier doit contenir 'sku_id' et 'quantity_out'.")

        # Calcul de la rotation
        rotation = df.groupby('sku_id')['quantity_out'].sum().reset_index()
        rotation = rotation.sort_values(by='quantity_out', ascending=False)
        
        # Calcul du cumulatif
        total_out = rotation['quantity_out'].sum()
        rotation['cum_percentage'] = 100 * rotation['quantity_out'].cumsum() / total_out
        
        # Attribution des classes
        def assign_class(pct):
            if pct <= 80: return 'A'
            elif pct <= 95: return 'B'
            else: return 'C'
            
        rotation['abc_class'] = rotation['cum_percentage'].apply(assign_class)
        return rotation

    def suggest_relocation(self, abc_results):
        """Génère des recommandations de réorganisation pour les produits A."""
        return abc_results[abc_results['abc_class'] == 'A'].to_dict(orient='records')

if __name__ == "__main__":
    print("Warehouse Management Module (WMS 4.0) Ready.")
