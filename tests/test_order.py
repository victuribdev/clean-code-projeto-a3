from src.models.order import Order
from src.services.order_service import OrderService
from src.services.customer_service import CustomerService
from src.services.product_service import ProductService

def test_order_creation(customer_service, product_service):
    # Cria um cliente e um produto
    customer = customer_service.add_customer(1, "John Doe", "john@email.com", "123456789")
    product = product_service.add_product(1, "Test Product", 10.99, 100)
    
    # Cria um pedido
    order = Order(1, customer)
    order.add_item(product, 2)
    
    assert order.id == 1
    assert order.customer.name == "John Doe"
    assert len(order.items) == 1
    assert order.items[0].product.name == "Test Product"
    assert order.items[0].quantity == 2

def test_order_total(order_service, customer_service, product_service):
    # Cria um cliente e produtos
    customer = customer_service.add_customer(1, "John Doe", "john@email.com", "123456789")
    product1 = product_service.add_product(1, "Product 1", 10.99, 100)
    product2 = product_service.add_product(2, "Product 2", 20.99, 100)
    
    # Cria um pedido com múltiplos itens
    order = order_service.create_order(1, customer)
    order.add_item(product1, 2)  # 2 unidades do Product 1
    order.add_item(product2, 3)  # 3 unidades do Product 2
    
    # Verifica o total
    assert order.total == (10.99 * 2) + (20.99 * 3)

def test_order_status(order_service, customer_service):
    # Cria um cliente e um pedido
    customer = customer_service.add_customer(1, "John Doe", "john@email.com", "123456789")
    order = order_service.create_order(1, customer)
    
    # Verifica status inicial
    assert order.status == "pending"
    
    # Atualiza status
    order_service.update_status(1, "completed")
    assert order.status == "completed"

def test_order_list(order_service, customer_service):
    # Cria um cliente
    customer = customer_service.add_customer(1, "John Doe", "john@email.com", "123456789")
    
    # Cria múltiplos pedidos
    order_service.create_order(1, customer)
    order_service.create_order(2, customer)
    
    # Verifica a lista de pedidos
    orders = order_service.list_orders()
    assert len(orders) == 2
    assert orders[0].id == 1
    assert orders[1].id == 2 