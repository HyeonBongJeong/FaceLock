from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import DetailView

from . import views
from .views import *
app_name = 'blog'

urlpatterns = [
path('blogs/', views.blog_list, name='blog_list'),
path('blogs/upload/', views.upload_blog, name='upload_blog'),
path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)