from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('blog:home')
#         else:
#             return render(request, 'registration/login.html', {'error': 'username or password is incorrect.'})
#     else:
#         return render(request, 'registration/login.html')


# def logout(request):
#     if request.method == "POST":
#         auth.logout(request)
#         return redirect('/')
#     return render(request, 'accounts/signup.html')
