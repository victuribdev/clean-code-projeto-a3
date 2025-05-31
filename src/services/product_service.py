from typing import List, Optional
from ..models.product import Product

class ProductService:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, id: int, name: str, price: float, stock: int) -> Product:
        """
        Adiciona um novo produto.
        
        Args:
            id: Identificador do produto
            name: Nome do produto
            price: Preço do produto
            stock: Quantidade em estoque
            
        Returns:
            Product: O produto criado
        """
        product = Product(id, name, price, stock)
        self.products.append(product)
        return product

    def get_product(self, id: int) -> Optional[Product]:
        """Retorna um produto pelo identificador."""
        for product in self.products:
            if product.id == id:
                return product
        return None

    def update_product(self, id: int, name: str, price: float, stock: int) -> bool:
        """
        Atualiza um produto existente.
        
        Args:
            id: Identificador do produto
            name: Novo nome do produto
            price: Novo preço do produto
            stock: Nova quantidade em estoque
            
        Returns:
            bool: True se atualizado com sucesso
        """
        product = self.get_product(id)
        if product:
            product.name = name
            product.price = price
            product.stock = stock
            return True
        return False

    def delete_product(self, id: int) -> bool:
        """
        Remove um produto existente.
        
        Args:
            id: Identificador do produto
            
        Returns:
            bool: True se removido com sucesso
        """
        product = self.get_product(id)
        if product:
            self.products.remove(product)
            return True
        return False

    def list_products(self) -> List[Product]:
        """Retorna todos os produtos cadastrados."""
        return self.products

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retorna todos os produtos de uma categoria."""
        return [p for p in self.products if p.category == category]

    def get_low_stock_products(self, threshold: int = 5) -> List[Product]:
        """Retorna produtos com estoque baixo."""
        return [p for p in self.products if p.quantity <= threshold] 