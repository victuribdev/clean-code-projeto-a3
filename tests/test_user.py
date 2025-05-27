import unittest
from refactored.models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("admin", "1234", "admin")
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.password, "1234")
        self.assertEqual(user.type, "admin")

if __name__ == "__main__":
    unittest.main() 