from typing import List, Optional
from ..models.order import Order
from ..models.customer import Customer
from ..models.product import Product

class OrderService:
    def __init__(self):
        self.orders: List[Order] = []
        self._next_id = 1
        self._customers: List[Customer] = []
        self._products: List[Product] = []

    def create_order(self, id: int, customer: Customer) -> Order:
        order = Order(id, customer)
        self.orders.append(order)
        return order

    def add_item(self, order_id: int, product_id: int, quantity: int) -> bool:
        order = self.get_order(order_id)
        product = self._find_product(product_id)
        if order and product and product.stock >= quantity:
            order.add_item(product, quantity)
            product.stock -= quantity
            return True
        return False

    def get_order(self, id: int) -> Optional[Order]:
        for order in self.orders:
            if order.id == id:
                return order
        return None

    def update_status(self, order_id: int, new_status: str) -> bool:
        order = self.get_order(order_id)
        if order:
            order.update_status(new_status)
            return True
        return False

    def list_orders(self) -> List[Order]:
        return self.orders

    def _find_product(self, id: int) -> Optional[Product]:
        for product in self._products:
            if product.id == id:
                return product
        return None 