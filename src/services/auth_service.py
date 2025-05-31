from typing import Optional, List
from ..models.user import User

class AuthService:
    def __init__(self):
        self.users: List[User] = []
        self.current_user: Optional[User] = None

    def add_user(self, username: str, password: str, user_type: str) -> User:
        """
        Adiciona um novo usuário.
        
        Args:
            username: Nome do usuário
            password: Senha do usuário
            user_type: Tipo do usuário (admin, vendedor)
            
        Returns:
            User: O usuário criado
        """
        # Verificar se usuário já existe
        if self.get_user(username):
            raise ValueError(f"Usuário {username} já existe")
            
        user = User(username, password, user_type)
        self.users.append(user)
        return user

    def login(self, username: str, password: str) -> bool:
        """
        Realiza login de um usuário.
        
        Args:
            username: Nome do usuário
            password: Senha do usuário
            
        Returns:
            bool: True se login bem sucedido
        """
        user = self.get_user(username)
        if user and user.password == password:
            self.current_user = user
            return True
        return False

    def logout(self) -> None:
        """Realiza logout do usuário atual."""
        self.current_user = None

    def get_user(self, username: str) -> Optional[User]:
        """Retorna um usuário pelo nome."""
        for user in self.users:
            if user.username == username:
                return user
        return None

    def is_admin(self) -> bool:
        """Verifica se o usuário atual é admin."""
        return self.current_user and self.current_user.type == "admin"

    def is_seller(self) -> bool:
        """Verifica se o usuário atual é vendedor."""
        return self.current_user and self.current_user.type == "vendedor"

    def is_authenticated(self) -> bool:
        """Verifica se há um usuário autenticado."""
        return self.current_user is not None 