from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path('signup/',views.signup_users, name='signup_users')
]