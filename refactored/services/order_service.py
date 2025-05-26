from typing import List, Dict, Optional
from decimal import Decimal
from ..models.order import Order, OrderItem
from ..models.product import Product
from ..models.customer import Customer

class OrderService:
    def __init__(self):
        self.orders: List[Order] = []
        self._current_order_id: int = 0

    def create_order(self, customer: Customer, items: List[Dict], payment_type: str) -> Optional[int]:
        """
        Cria um novo pedido.
        
        Args:
            customer: Cliente que está fazendo o pedido
            items: Lista de itens do pedido
            payment_type: Tipo de pagamento
            
        Returns:
            ID do pedido criado ou None se houver erro
        """
        try:
            order = Order(customer.name, items, payment_type)
            self.orders.append(order)
            customer.add_order(self._current_order_id)
            order_id = self._current_order_id
            self._current_order_id += 1
            return order_id
        except Exception as e:
            print(f"Erro ao criar pedido: {str(e)}")
            return None

    def get_order(self, order_id: int) -> Optional[Order]:
        """
        Retorna um pedido pelo ID.
        
        Args:
            order_id: ID do pedido
            
        Returns:
            Pedido encontrado ou None
        """
        if 0 <= order_id < len(self.orders):
            return self.orders[order_id]
        return None

    def update_order_status(self, order_id: int, new_status: str) -> bool:
        """
        Atualiza o status de um pedido.
        
        Args:
            order_id: ID do pedido
            new_status: Novo status
            
        Returns:
            True se atualizado com sucesso, False caso contrário
        """
        order = self.get_order(order_id)
        if order:
            order.update_status(new_status)
            return True
        return False

    def get_customer_orders(self, customer: Customer) -> List[Order]:
        """
        Retorna todos os pedidos de um cliente.
        
        Args:
            customer: Cliente
            
        Returns:
            Lista de pedidos do cliente
        """
        return [self.orders[order_id] for order_id in customer.get_order_history()]

    def calculate_order_total(self, order: Order) -> Decimal:
        """
        Calcula o total de um pedido.
        
        Args:
            order: Pedido
            
        Returns:
            Total do pedido
        """
        return order.total

    def get_order_summary(self, order_id: int) -> Optional[Dict]:
        """
        Retorna um resumo do pedido.
        
        Args:
            order_id: ID do pedido
            
        Returns:
            Resumo do pedido ou None
        """
        order = self.get_order(order_id)
        if order:
            return order.get_summary()
        return None 