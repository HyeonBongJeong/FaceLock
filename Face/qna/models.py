from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models
# Create your models here.
from django.shortcuts import redirect
from django.utils import timezone


password_validators = MaxLengthValidator(4, "문자, 숫자 조합 상관없이 4글자 까지만 입력해주세요")

class QnA(models.Model):
    q_title = models.CharField(max_length=200)
    q_password = models.CharField(max_length=4, validators=[password_validators], null=True)
    q_date = models.DateTimeField(auto_now=True)
    q_data = models.TextField(blank=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.q_title

class Comment(models.Model):
    QnA = models.ForeignKey(QnA, on_delete=models.CASCADE, null=True, related_name='comments')
    comment = models.CharField(max_length=200, blank=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)







