from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField("닉네임", max_length=20, null=True)
    profile_image = models.ImageField(
        "프로필 사진", blank=True, upload_to='user/profile_pic')
    introduce = models.TextField(
        "자기 소개", blank=True, help_text='자기 소개를 작성하세요.')

    def __str__(self):
        return self.user.username
