from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects # blog 안의 데이터들, 모델로부터 전달받은 객체 목록: 쿼리셋, 쿼리셋 처리해주는 방법: 메소드
    return render(request, 'blog/home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id) # object를 가져오고 없으면 404 에러를 띄우는 함수, 안에 모델명과 blog 게시글 id 적으면 됨
                                                    # pk란 모델에서 찍어낸 수많은 객체들을 구분할 수 있는 구분자
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def post(request):
    return render(request, 'blog/post.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))