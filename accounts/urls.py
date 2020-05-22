from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name="accountssignup"),
    path('login', views.login, name="accountslogin"),
]
