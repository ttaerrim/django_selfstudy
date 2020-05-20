from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects # blog 안의 데이터들, 모델로부터 전달받은 객체 목록: 쿼리셋, 쿼리셋 처리해주는 방법: 메소드
    return render(request, 'blog/home.html', {'blogs': blogs})