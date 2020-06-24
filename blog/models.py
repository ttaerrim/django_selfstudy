from django.db import models

# username: qshp
# email: ltr0121@likelion.org
# password: 1234

# Create your models here.


class Blog(models.Model):
    title = models.CharField("제목", max_length=200)  # 최대 200자 문자열
    pub_date = models.DateTimeField('date published')  # 날짜와 시간
    body = models.TextField("내용")  # 긴 문자열
    writer = models.CharField(max_length=100, blank=True)
    profile_image_url = models.URLField(blank=True, max_length=200)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
