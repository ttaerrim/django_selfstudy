from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Blog, Comment
from .forms import BlogPost, CommentForm
from accounts.models import Profile
# Create your views here.


def home(request):
    blogs = Blog.objects  # blog 안의 데이터들, 모델로부터 전달받은 객체 목록: 쿼리셋, 쿼리셋 처리해주는 방법: 메소드
    # .order_by('-id')는 글 순서 최신 순으로
    blog_list = Blog.objects.order_by('-id')  # 블로그 모든 글을 불러와서
    paginator = Paginator(blog_list, 5)  # 블로그 객체 세 개를 한 페이지로 자르기
    # request된 페이지 뭔지 알아내고 (request 페이지를 변수에 담음)
    page = request.GET.get('page')
    posts = paginator.get_page(page)  # request된 페이지 얻어와서 return
    return render(request, 'blog/home.html', {'blogs': blogs, 'posts': posts})


def detail(request, blog_id):
    # object를 가져오고 없으면 404 에러를 띄우는 함수, 안에 모델명과 blog 게시글 id 적으면 됨
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # pk란 모델에서 찍어낸 수많은 객체들을 구분할 수 있는 구분자
    comments = Comment.objects
    return render(request, 'blog/detail.html', {'blog': blog_detail, 'comments': comments})


def post(request):
    return render(request, 'blog/post.html')


def create(request):  # model 사용
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))


@login_required
def blogpost(request):  # form 사용
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            conn_user = request.user
            conn_profile = Profile.objects.get(user=conn_user)
            nickname = conn_profile.nickname

            if not conn_profile.profile_image:
                pic_url = ""
            else:
                pic_url = conn_profile.profile_image.url

            post = form.save(commit=False)
            post.writer = nickname
            post.profile_image_url = pic_url
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:home')
    else:
        form = BlogPost()
        return render(request, 'blog/new.html', {'form': form})


@login_required
def edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogPost(request.POST, instance=post)
        conn_user = request.user
        nickname = Profile.objects.get(user=conn_user)
        if nickname != post.writer:
            messages.info(request, '수정할 수 없습니다')
            return HttpResponseRedirect(reverse_lazy('blog_index'))

        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:home')
    else:
        form = BlogPost(instance=post)
        return render(request, 'blog/edit.html', {'form': form})


def delete(request, pk):
    blog = Blog.objects.get(id=pk)
    if form.is_valid():
        conn_user = request.user
    blog.delete()
    return redirect('blog:home')


def comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            conn_user = request.user
            form.author = Profile.objects.get(user=conn_user)

            form = form.save(commit=False)
            form.blog = blog
            form.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {'form': form})
