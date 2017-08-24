from app import connect_db
from mongoengine.connection import _get_db
import unittest

from models.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        connect_db(db="test-temp")

    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def user_dict(self):
        return dict(
            first_name="Jorge",
            last_name="Escobar",
            username="jorge",
            email="jorge@example.com",
            password="test123",
            confirm="test123"
        )

    def test_create_user(self):
        user = User(self.user_dict())
        
        user.save()
       
        assert User.objects.filter(username=self.user_dict()[
                                   'username']).count() == 1

        