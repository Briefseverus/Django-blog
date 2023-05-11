from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
