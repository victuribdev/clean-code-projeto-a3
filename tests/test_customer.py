from src.models.customer import Customer
from src.services.customer_service import CustomerService

def test_customer_creation():
    customer = Customer(1, "John Doe", "john@email.com", "123456789")
    assert customer.id == 1
    assert customer.name == "John Doe"
    assert customer.email == "john@email.com"
    assert customer.phone == "123456789"

def test_customer_update(customer_service):
    # Adiciona um cliente
    customer_service.add_customer(1, "John Doe", "john@email.com", "123456789")
    
    # Atualiza o cliente
    customer_service.update_customer(1, "John Updated", "john.updated@email.com", "987654321")
    
    # Verifica se foi atualizado
    customer = customer_service.get_customer(1)
    assert customer.name == "John Updated"
    assert customer.email == "john.updated@email.com"
    assert customer.phone == "987654321"

def test_customer_delete(customer_service):
    # Adiciona um cliente
    customer_service.add_customer(1, "John Doe", "john@email.com", "123456789")
    
    # Deleta o cliente
    customer_service.delete_customer(1)
    
    # Verifica se foi deletado
    assert customer_service.get_customer(1) is None

def test_customer_list(customer_service):
    # Adiciona alguns clientes
    customer_service.add_customer(1, "John Doe", "john@email.com", "123456789")
    customer_service.add_customer(2, "Jane Doe", "jane@email.com", "987654321")
    
    # Verifica se a lista está correta
    customers = customer_service.list_customers()
    assert len(customers) == 2
    assert customers[0].name == "John Doe"
    assert customers[1].name == "Jane Doe" 