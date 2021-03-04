from django.contrib import admin
from qna.models import QnA, Comment


# Register your models here.

class QnaAdmin(admin.ModelAdmin):
    list_display = ('q_title', 'member')

admin.site.register(QnA)
admin.site.register(Comment)
