from django.contrib.auth.decorators import login_required
from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>/', login_required(views.ProfileView.as_view()), name='profile'),
    path('change_password/', views.change_password, name='change_password'),



]