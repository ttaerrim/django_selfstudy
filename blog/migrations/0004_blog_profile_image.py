# Generated by Django 2.2.1 on 2020-06-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200623_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='user/profile_pic'),
        ),
    ]