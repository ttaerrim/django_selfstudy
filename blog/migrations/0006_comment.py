# Generated by Django 2.2.1 on 2020-06-28 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_profile_image'),
        ('blog', '0005_auto_20200624_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_body', models.CharField(max_length=200)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Blog')),
                ('comment_writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
