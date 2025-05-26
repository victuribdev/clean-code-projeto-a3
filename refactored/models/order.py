from typing import List, Dict
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class OrderItem:
    product_name: str
    quantity: int
    price: Decimal
    total: Decimal

class Order:
    def __init__(self, customer_name: str, items: List[Dict], payment_type: str):
        self.customer = customer_name
        self.items: List[OrderItem] = []
        self.payment_type = payment_type
        self.status = "pendente"
        self.subtotal: Decimal = Decimal('0')
        self.discount: Decimal = Decimal('0')
        self.tax: Decimal = Decimal('0')
        self.total: Decimal = Decimal('0')
        
        self._process_items(items)
        self._calculate_totals()

    def _process_items(self, items: List[Dict]) -> None:
        """Processa os itens do pedido."""
        for item in items:
            order_item = OrderItem(
                product_name=item['product'],
                quantity=item['quantity'],
                price=Decimal(str(item['price'])),
                total=Decimal(str(item['total']))
            )
            self.items.append(order_item)

    def _calculate_totals(self) -> None:
        """Calcula os totais do pedido."""
        # Calcula subtotal
        self.subtotal = sum(item.total for item in self.items)
        
        # Aplica desconto se o total for maior que 1000
        if self.subtotal > Decimal('1000'):
            self.discount = self.subtotal * Decimal('0.05')
            self.subtotal -= self.discount
        
        # Calcula imposto
        self.tax = self.subtotal * Decimal('0.1')
        
        # Calcula total final
        self.total = self.subtotal + self.tax

    def update_status(self, new_status: str) -> None:
        """Atualiza o status do pedido."""
        self.status = new_status

    def get_summary(self) -> Dict:
        """Retorna um resumo do pedido."""
        return {
            "customer": self.customer,
            "items": [
                {
                    "product": item.product_name,
                    "quantity": item.quantity,
                    "price": float(item.price),
                    "total": float(item.total)
                }
                for item in self.items
            ],
            "subtotal": float(self.subtotal),
            "discount": float(self.discount),
            "tax": float(self.tax),
            "total": float(self.total),
            "payment_type": self.payment_type,
            "status": self.status
        } 