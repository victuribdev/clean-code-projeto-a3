class User:
    def __init__(self, username: str, password: str, user_type: str):
        self.username = username
        self.password = password
        self.type = user_type

class AuthService:
    def __init__(self):
        self.users = []
        self.current_user = None

    def add_user(self, username: str, password: str, user_type: str) -> None:
        # Implementação
        
    def login(self, username: str, password: str) -> bool:
        # Implementação
        
    def logout(self) -> None:
        self.current_user = None