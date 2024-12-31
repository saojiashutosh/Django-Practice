from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField("Username", max_length=10)
    password = models.CharField("Password", max_length=16)
    name =  models.CharField("Name", max_length=20)
    contact = models.CharField("Contact", max_length=10)
    image = models.ImageField("Image",upload_to = "images/")

    def __str__(self):
        return self.name