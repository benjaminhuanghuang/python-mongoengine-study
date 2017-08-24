from mongoengine import *

class User(Document):
    username = StringField(db_field="username", required=True, unique=True)
    password = StringField(db_field="password", required=True)
    email = EmailField(db_field="email", required=True, unique=True)
