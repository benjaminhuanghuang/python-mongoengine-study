from app import connect_db
from mongoengine.connection import _get_db
from mongoengine import *

import unittest

from models.user import User



class UserTest(unittest.TestCase):
    def setUp(self):
        self.db_client = connect_db(db="test-temp")

    def tearDown(self):
        db = _get_db()
        self.db_client.drop_database(db)

    def user_dict(self):
        return dict(
            username="jorge",
            email="jorge@example.com",
            password="test123"
        )

    def test_create_user(self):
        default_user = self.user_dict()
        user = User(username = default_user['username'],
                    email = default_user['email'],
                    password = default_user['password'])
        
        user.save()
       
        assert User.objects.filter(username=self.user_dict()[
                                   'username']).count() == 1

        