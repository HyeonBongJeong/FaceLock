
from django.db import models
# Create your models here.
from django.db import models



class Notices(models.Model):
    notice_title = models.CharField(max_length=200)
    notice_date = models.DateTimeField('date published')
    notice_count = models.IntegerField(default=0)
    notice_text = models.TextField(blank=True)

