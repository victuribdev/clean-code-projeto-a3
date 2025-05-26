from typing import Optional

class Product:
    def __init__(self, name: str, category: str, price: float, quantity: int):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity: int) -> None:
        """Atualiza a quantidade do produto."""
        self.quantity += quantity

    def has_sufficient_stock(self, requested_quantity: int) -> bool:
        """Verifica se há estoque suficiente do produto."""
        return self.quantity >= requested_quantity

    def calculate_discount(self) -> float:
        """Calcula o desconto do produto baseado em sua categoria."""
        if self.category == "eletrônicos":
            return 0.9  # 10% de desconto
        return 1.0  # Sem desconto 