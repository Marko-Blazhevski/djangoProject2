from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
