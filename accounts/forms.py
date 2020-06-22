from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', ]


class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'profile': ProfileForm,
    }
