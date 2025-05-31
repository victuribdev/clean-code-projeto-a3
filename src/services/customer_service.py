from typing import List, Optional
from ..models.customer import Customer

class CustomerService:
    def __init__(self):
        self.customers: List[Customer] = []

    def add_customer(self, id: int, name: str, email: str, phone: str) -> Customer:
        """
        Adiciona um novo cliente.
        
        Args:
            id: ID do cliente
            name: Nome do cliente
            email: Email do cliente
            phone: Telefone do cliente
            
        Returns:
            Customer: O cliente criado
        """
        customer = Customer(id, name, email, phone)
        self.customers.append(customer)
        return customer

    def get_customer(self, id: int) -> Optional[Customer]:
        """Retorna um cliente pelo ID."""
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None

    def update_customer(self, id: int, name: str, email: str, phone: str) -> bool:
        """
        Atualiza os dados de um cliente.
        
        Args:
            id: ID do cliente
            name: Novo nome do cliente
            email: Novo email do cliente
            phone: Novo telefone do cliente
            
        Returns:
            bool: True se atualizado com sucesso
        """
        customer = self.get_customer(id)
        if customer:
            customer.name = name
            customer.email = email
            customer.phone = phone
            return True
        return False

    def delete_customer(self, id: int) -> bool:
        customer = self.get_customer(id)
        if customer:
            self.customers.remove(customer)
            return True
        return False

    def get_customer_orders(self, name: str) -> List:
        """Retorna todos os pedidos de um cliente."""
        customer = self.get_customer(name)
        if customer:
            return customer.orders
        return []

    def list_customers(self) -> List[Customer]:
        """Retorna todos os clientes."""
        return self.customers 