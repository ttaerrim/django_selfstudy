from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="wchome"),
    path('about/', views.about, name="wcabout"),
    path('count/', views.count, name="wccount"),
]
