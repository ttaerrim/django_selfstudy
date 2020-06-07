from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="bloghome"),
    # path-converter <type:name> 같은 모양
    path('<int:blog_id>', views.detail, name="blogdetail"),
    path('newblog/', views.blogpost, name='blognow'),
    path('post/', views.post, name="blogpost"),
    path('create/', views.create, name="blogcreate"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
