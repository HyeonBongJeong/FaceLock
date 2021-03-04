
from django.urls import path
from . import views
from .views import *

app_name = 'notice'

urlpatterns = [
    path('list', NoticesListView.as_view(), name='List'),
    path('detail/<int:pk>/', NoticesDetailView.as_view(), name='Detail'),





]