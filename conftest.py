import pytest
from src.services.auth_service import AuthService
from src.services.customer_service import CustomerService
from src.services.product_service import ProductService
from src.services.order_service import OrderService

@pytest.fixture
def auth_service():
    return AuthService()

@pytest.fixture
def customer_service():
    return CustomerService()

@pytest.fixture
def product_service():
    return ProductService()

@pytest.fixture
def order_service():
    return OrderService() 