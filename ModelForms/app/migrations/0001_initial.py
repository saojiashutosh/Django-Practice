# Generated by Django 5.1.4 on 2024-12-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, verbose_name='Username')),
                ('password', models.CharField(max_length=16, verbose_name='Password')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('contact', models.CharField(max_length=10, verbose_name='Contact')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
            ],
        ),
    ]