from typing import List

class Customer:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.orders: List[int] = []  # Lista de IDs de pedidos

    def add_order(self, order_id: int) -> None:
        """Adiciona um pedido ao histórico do cliente."""
        self.orders.append(order_id)

    def get_order_history(self) -> List[int]:
        """Retorna o histórico de pedidos do cliente."""
        return self.orders 