from typing import List, Dict

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Order:
    def __init__(self, id: int, customer):
        self.id = id
        self.customer = customer
        self.items: List[OrderItem] = []
        self.status = "pending"
        self.total = 0.0

    def add_item(self, product, quantity):
        self.items.append(OrderItem(product, quantity))
        self.calculate_total()

    def calculate_total(self):
        self.total = sum(item.product.price * item.quantity for item in self.items)

    def update_status(self, status: str):
        self.status = status

    def __calculate_totals(self):
        # Implementar lógica de cálculos (subtotal, desconto, etc)
        pass