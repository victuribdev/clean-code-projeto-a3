from typing import List, Dict, Any
from ..models.order import Order
from ..models.product import Product
from ..models.customer import Customer

class ReportService:
    def __init__(self, orders: List[Order], products: List[Product], customers: List[Customer]):
        self.orders = orders
        self.products = products
        self.customers = customers

    def sales_report(self) -> List[Dict[str, Any]]:
        """
        Gera um relatório de vendas com informações dos pedidos.
        Returns:
            Lista de dicionários com resumo das vendas
        """
        report = []
        for order in self.orders:
            report.append({
                'order_id': order.id,
                'customer': order.customer.name,
                'total': order.get_total(),
                'status': order.status
            })
        return report

    def customers_report(self) -> List[Dict[str, Any]]:
        """
        Gera um relatório de clientes com informações básicas e histórico de pedidos.
        Returns:
            Lista de dicionários com dados dos clientes
        """
        report = []
        for customer in self.customers:
            report.append({
                'name': customer.name,
                'email': customer.email,
                'address': customer.address,
                'orders': customer.get_order_history()
            })
        return report

    def stock_report(self) -> List[Dict[str, Any]]:
        """
        Gera um relatório de produtos em estoque.
        Returns:
            Lista de dicionários com dados dos produtos
        """
        report = []
        for product in self.products:
            report.append({
                'name': product.name,
                'category': product.category,
                'stock': product.stock,
                'price': product.price
            })
        return report 