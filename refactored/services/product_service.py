from typing import List, Dict, Optional
from decimal import Decimal
from ..models.product import Product

class ProductService:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, name: str, category: str, price: float, quantity: int) -> Optional[Product]:
        """
        Adiciona um novo produto.
        
        Args:
            name: Nome do produto
            category: Categoria do produto
            price: Preço do produto
            quantity: Quantidade em estoque
            
        Returns:
            Produto criado ou None se houver erro
        """
        try:
            product = Product(name, category, price, quantity)
            self.products.append(product)
            return product
        except Exception as e:
            print(f"Erro ao adicionar produto: {str(e)}")
            return None

    def get_product(self, name: str) -> Optional[Product]:
        """
        Retorna um produto pelo nome.
        
        Args:
            name: Nome do produto
            
        Returns:
            Produto encontrado ou None
        """
        for product in self.products:
            if product.name == name:
                return product
        return None

    def update_stock(self, product_name: str, quantity: int) -> bool:
        """
        Atualiza o estoque de um produto.
        
        Args:
            product_name: Nome do produto
            quantity: Quantidade a ser adicionada/removida
            
        Returns:
            True se atualizado com sucesso, False caso contrário
        """
        product = self.get_product(product_name)
        if product:
            product.update_quantity(quantity)
            return True
        return False

    def check_stock(self, product_name: str, requested_quantity: int) -> bool:
        """
        Verifica se há estoque suficiente de um produto.
        
        Args:
            product_name: Nome do produto
            requested_quantity: Quantidade solicitada
            
        Returns:
            True se há estoque suficiente, False caso contrário
        """
        product = self.get_product(product_name)
        if product:
            return product.has_sufficient_stock(requested_quantity)
        return False

    def get_products_by_category(self, category: str) -> List[Product]:
        """
        Retorna todos os produtos de uma categoria.
        
        Args:
            category: Categoria dos produtos
            
        Returns:
            Lista de produtos da categoria
        """
        return [p for p in self.products if p.category == category]

    def get_low_stock_products(self, threshold: int = 10) -> List[Product]:
        """
        Retorna produtos com estoque baixo.
        
        Args:
            threshold: Limite de estoque baixo
            
        Returns:
            Lista de produtos com estoque baixo
        """
        return [p for p in self.products if p.quantity < threshold]

    def apply_discount(self, product_name: str) -> Optional[float]:
        """
        Aplica desconto a um produto.
        
        Args:
            product_name: Nome do produto
            
        Returns:
            Fator de desconto ou None
        """
        product = self.get_product(product_name)
        if product:
            return product.calculate_discount()
        return None 