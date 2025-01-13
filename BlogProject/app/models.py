from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField("Username", max_length=10 ,unique=True)
    password = models.CharField("Password", max_length=16)
    name =  models.CharField("Name", max_length=20)
    contact = models.CharField("Contact", max_length=10,)
    image = models.ImageField("Image",upload_to = "images/")

    def __str__(self):
        return f"{self.name}"
    
class blog(models.Model):
    title = models.CharField("Title", max_length=50)
    content = models.TextField("Content",max_length=500)
    pub_date = models.DateTimeField("Published On", auto_now_add=True)
    name =  models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}   {self.name}    {self.pub_date}"