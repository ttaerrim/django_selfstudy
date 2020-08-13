from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name="home"),
    # path-converter <type:name> 같은 모양
    path('<int:blog_id>', views.detail, name="detail"),
    path('newblog/', views.blogpost, name='now'),
    path('post/', views.post, name="post"),
    path('create/', views.create, name="create"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'), path(
        'comment/<int:pk>/', views.comment, name='comment'),
]
