import unittest
from refactored.models.customer import Customer

class TestCustomer(unittest.TestCase):
    def test_customer_creation(self):
        customer = Customer("João", "Rua 1", "joao@email.com")
        self.assertEqual(customer.name, "João")
        self.assertEqual(customer.address, "Rua 1")
        self.assertEqual(customer.email, "joao@email.com")
        self.assertEqual(customer.orders, [])

if __name__ == "__main__":
    unittest.main() 