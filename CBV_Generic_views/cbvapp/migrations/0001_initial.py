# Generated by Django 5.1.4 on 2024-12-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='User Name')),
                ('review', models.TextField(max_length=250, verbose_name='Review')),
                ('rating', models.IntegerField(default=1, verbose_name='Rating')),
            ],
        ),
    ]
