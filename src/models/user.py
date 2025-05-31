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
        self.users.append({"username": username, "password": password, "type": user_type})
        
    def login(self, username: str, password: str) -> bool:
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                self.current_user = user
                return True
        return False
        
    def logout(self) -> None:
        self.current_user = None