from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=10000)
    active=models.BooleanField()
    publish_date=models.DateTimeField()

    def __str__(self):
        return self.title
