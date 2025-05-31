import unittest
from refactored.models.product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product("Caderno", 15.5, 10)
        self.assertEqual(product.name, "Caderno")
        self.assertEqual(product.price, 15.5)
        self.assertEqual(product.quantity, 10)

if __name__ == "__main__":
    unittest.main() 