import unittest
from refactored.models.order import Order

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        items = [
            {"product": "Produto A", "quantity": 2, "price": 10.0},
            {"product": "Produto B", "quantity": 1, "price": 20.0}
        ]
        order = Order("Cliente 1", items, "credit_card")
        self.assertEqual(order.customer, "Cliente 1")
        self.assertEqual(order.items, items)
        self.assertEqual(order.payment_type, "credit_card")
        self.assertEqual(order.status, "pending")

if __name__ == "__main__":
    unittest.main() 