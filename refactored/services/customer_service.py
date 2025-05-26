from typing import List, Dict, Optional
from ..models.customer import Customer
from ..models.order import Order

class CustomerService:
    def __init__(self):
        self.customers: List[Customer] = []

    def register_customer(self, name: str, address: str, email: str) -> Optional[Customer]:
        """
        Registra um novo cliente.
        
        Args:
            name: Nome do cliente
            address: Endereço do cliente
            email: Email do cliente
            
        Returns:
            Cliente criado ou None se houver erro
        """
        try:
            customer = Customer(name, address, email)
            self.customers.append(customer)
            return customer
        except Exception as e:
            print(f"Erro ao registrar cliente: {str(e)}")
            return None

    def get_customer(self, name: str) -> Optional[Customer]:
        """
        Retorna um cliente pelo nome.
        
        Args:
            name: Nome do cliente
            
        Returns:
            Cliente encontrado ou None
        """
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def get_customer_by_email(self, email: str) -> Optional[Customer]:
        """
        Retorna um cliente pelo email.
        
        Args:
            email: Email do cliente
            
        Returns:
            Cliente encontrado ou None
        """
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None

    def update_customer_address(self, name: str, new_address: str) -> bool:
        """
        Atualiza o endereço de um cliente.
        
        Args:
            name: Nome do cliente
            new_address: Novo endereço
            
        Returns:
            True se atualizado com sucesso, False caso contrário
        """
        customer = self.get_customer(name)
        if customer:
            customer.address = new_address
            return True
        return False

    def update_customer_email(self, name: str, new_email: str) -> bool:
        """
        Atualiza o email de um cliente.
        
        Args:
            name: Nome do cliente
            new_email: Novo email
            
        Returns:
            True se atualizado com sucesso, False caso contrário
        """
        customer = self.get_customer(name)
        if customer:
            customer.email = new_email
            return True
        return False

    def get_customer_orders(self, customer: Customer) -> List[int]:
        """
        Retorna os IDs dos pedidos de um cliente.
        
        Args:
            customer: Cliente
            
        Returns:
            Lista de IDs dos pedidos
        """
        return customer.get_order_history()

    def get_all_customers(self) -> List[Customer]:
        """
        Retorna todos os clientes.
        
        Returns:
            Lista de todos os clientes
        """
        return self.customers 