from django.db import models

# Create your models here.

class User:
    users_db = []
    def __init__(self, fullname=None,email=None,password=None):
        self.fullname = fullname
        self.email = email
        self.password = password

    def save_user(self): 
        self.users_db.append({
            'fullname':self.fullname,
            'email':self.email,
            'password':self.password
        })

    @staticmethod
    def get_all_users():
        return User.users_db

    