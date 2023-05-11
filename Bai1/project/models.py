from django.db import models



class pro(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    language = models.TextField()
    link = models.TextField()
    imgLink = models.CharField(max_length=2550, default='default-image.jpg')
    date = models.DateTimeField(auto_now_add=True)


    
