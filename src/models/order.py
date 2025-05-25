from typing import List, Dict

class Order:
    def __init__(self, customer_name: str, items: List[Dict], payment_type: str):
        self.customer = customer_name
        self.items = items  # Lista de dicionários {product, quantity, price}
        self.payment_type = payment_type
        self.status = "pending"
        self.__calculate_totals()
    
    def __calculate_totals(self):
        # Implementar lógica de cálculos (subtotal, desconto, etc)
        pass