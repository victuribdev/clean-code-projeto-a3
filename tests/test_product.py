from src.models.product import Product
from src.services.product_service import ProductService

def test_product_creation():
    product = Product(1, "Test Product", 10.99, 100)
    assert product.id == 1
    assert product.name == "Test Product"
    assert product.price == 10.99
    assert product.stock == 100

def test_product_update(product_service):
    # Adiciona um produto
    product_service.add_product(1, "Test Product", 10.99, 100)
    
    # Atualiza o produto
    product_service.update_product(1, "Updated Product", 15.99, 50)
    
    # Verifica se foi atualizado
    product = product_service.get_product(1)
    assert product.name == "Updated Product"
    assert product.price == 15.99
    assert product.stock == 50

def test_product_delete(product_service):
    # Adiciona um produto
    product_service.add_product(1, "Test Product", 10.99, 100)
    
    # Deleta o produto
    product_service.delete_product(1)
    
    # Verifica se foi deletado
    assert product_service.get_product(1) is None

def test_product_list(product_service):
    # Adiciona alguns produtos
    product_service.add_product(1, "Product 1", 10.99, 100)
    product_service.add_product(2, "Product 2", 20.99, 200)
    
    # Verifica se a lista está correta
    products = product_service.list_products()
    assert len(products) == 2
    assert products[0].name == "Product 1"
    assert products[1].name == "Product 2" 