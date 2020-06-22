from django.urls import path
from . import views

app_name = 'wc'
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('count/', views.count, name="count"),
]
