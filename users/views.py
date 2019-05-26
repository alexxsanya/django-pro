from django.shortcuts import render
import json
from django.http import HttpResponse
from users.models import User

def signup_users(request): 

    data = {
        'fullname':'Alex Ssanya',
        'email': 'alex@gmail.com',
        'password': 'Password'
    }

    User(**data).save_user()
    
    get_all_users = User.get_all_users()
    
    return HttpResponse(json.dumps(get_all_users))
