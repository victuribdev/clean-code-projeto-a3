from models.user import User

class OrderSystem:
    def __init__(self):
        self._users = [] # Lista de Usuários
        self._products = [] # Lista de Produtos
        self._orders = [] # Lista de Pedidos
        self._customers = []  # Lista de Clientes

    def add_user(self, username: str, password: str, user_type: str):
        self._users.append(User(username, password, user_type))
        print(f"Usuário {username} criado com sucesso.")