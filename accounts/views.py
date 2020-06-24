from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


from .forms import ProfileForm, UserCreationMultiForm
from .models import Profile
# Create your views here.


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class UserSignupView(generic.CreateView):
    form_class = UserCreationMultiForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = form['user'].save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()
        return redirect(self.success_url)


@login_required
def mypage(request):
    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)

    if not conn_profile.profile_image:
        pic_url = ""
    else:
        pic_url = conn_profile.profile_image.url

    context = {
        'id': conn_user.username,
        'nickname': conn_profile.nickname,
        'intro': conn_profile.introduce,
        'profile_pic': pic_url,
    }
    return render(request, 'accounts/mypage.html', context=context)
# def signup(request):
#     if request.method == "POST":
#         if request.POST["password1"] == request.POST["password2"]:
#             user = User.objects.create_user(
#                 username = request.POST["username"],
#                 password = request.POST["password1"]
#             )
#             nickname = request.POST["nickname"]
#             profile = Profile(user = user, nickname = nickname)
#             profile.save()
#             auth.login(request, user)
#             return redirect('account:login')
#     return render(request, 'account/signup.html')

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
