from typing import Optional, List, Dict

class User:
    def __init__(self, username: str, password: str, user_type: str):
        self.username = username
        self.password = password
        self.type = user_type

class AuthService:
    def __init__(self):
        self.users: List[User] = []
        self.current_user: Optional[User] = None
        self.language: str = "pt"

    def add_user(self, username: str, password: str, user_type: str) -> None:
        """Adiciona um novo usuário ao sistema."""
        self.users.append(User(username, password, user_type))
        if self.language == "pt":
            print(f"Usuário {username} criado com sucesso.")
        else:
            print(f"User {username} created successfully.")

    def login(self, username: str, password: str) -> bool:
        """Realiza o login do usuário."""
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                if self.language == "pt":
                    print(f"Bem-vindo, {username}!")
                else:
                    print(f"Welcome, {username}!")
                return True
        
        if self.language == "pt":
            print("Credenciais inválidas.")
        else:
            print("Invalid credentials.")
        return False

    def logout(self) -> None:
        """Realiza o logout do usuário atual."""
        self.current_user = None
        if self.language == "pt":
            print("Logout realizado com sucesso.")
        else:
            print("Logout successful.")

    def change_language(self, language: str) -> None:
        """Altera o idioma do sistema."""
        if language in ["pt", "en"]:
            self.language = language
            if self.language == "pt":
                print("Idioma alterado para português.")
            else:
                print("Language changed to English.")
        else:
            if self.language == "pt":
                print("Idioma não suportado.")
            else:
                print("Language not supported.") 