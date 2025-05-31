from src.models.user import User
from src.services.auth_service import AuthService

def test_user_creation():
    user = User("admin", "1234", "admin")
    assert user.username == "admin"
    assert user.password == "1234"
    assert user.type == "admin"

def test_user_login(auth_service):
    # Primeiro adiciona um usuário
    auth_service.add_user("test_user", "test_pass", "user")
    
    # Testa login bem sucedido
    assert auth_service.login("test_user", "test_pass") is True
    assert auth_service.current_user is not None
    assert auth_service.current_user.username == "test_user"

def test_user_login_invalid_credentials(auth_service):
    # Testa login com credenciais inválidas
    assert auth_service.login("invalid_user", "invalid_pass") is False
    assert auth_service.current_user is None

def test_user_logout(auth_service):
    # Primeiro faz login
    auth_service.add_user("test_user", "test_pass", "user")
    auth_service.login("test_user", "test_pass")
    
    # Testa logout
    auth_service.logout()
    assert auth_service.current_user is None 