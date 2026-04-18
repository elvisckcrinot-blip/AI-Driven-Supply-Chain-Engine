import unittest
import pandas as pd
from src.warehouse_mgmt.slotting_optimizer import SlottingOptimizer
from src.transport_control.carbon_tracker import TransportTracker

class TestSCEngine(unittest.TestCase):
    
    def test_abc_segmentation(self):
        """Vérifie que la segmentation ABC classe bien les produits."""
        optimizer = SlottingOptimizer()
        data = pd.DataFrame({
            'sku_id': ['A', 'B', 'C'],
            'quantity_out': [1000, 100, 10]
        })
        optimizer.data = data
        results = optimizer.calculate_abc_segmentation()
        self.assertEqual(results.iloc[0]['abc_class'], 'A')

    def test_carbon_footprint(self):
        """Vérifie la précision du calcul CO2."""
        tracker = TransportTracker()
        # 10 tonnes * 100 km * 0.105 (truck) = 105.0
        emissions = tracker.calculate_carbon_footprint(10, 100, 'truck')
        self.assertEqual(emissions, 105.0)

if __name__ == '__main__':
    unittest.main()
      
