from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100)
    #author = models.CharField(max_length=100)
    text = models.TextField(default='내용이 없습니다.')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='blogs/files/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

