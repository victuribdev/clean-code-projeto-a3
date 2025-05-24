class Customer:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.orders = []  # Lista de IDs de pedidos