
from django.urls import path

import qna
from . import views
from .views import *

app_name = 'qna'

urlpatterns = [
    path('list', QnAListView.as_view(), name='List'),
    path('detail/<int:pk>/', QnADetailView.as_view(), name='detail'),
    path('delete/<int:pk>', QnADeleteView.as_view(), name='delete'),
    path('update/<int:pk>', QnAUpdateView.as_view(), name='update'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),


]