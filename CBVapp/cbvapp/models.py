from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField("User Name", max_length=50)
    review = models.TextField("Review",max_length=250)
    rating = models.IntegerField("Rating",default=1)

    def __str__(self):
        return self.name