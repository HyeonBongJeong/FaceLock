from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from account.views import register

app_name = 'account'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('findPwd/', views.FindPwd, name='findPwd'),
    path('findId/', views.FindId, name='findId'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
    path('id/find/', views.ajax_find_id_view, name='ajax_id'),




]
