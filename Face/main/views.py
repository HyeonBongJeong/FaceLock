from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.hashers import check_password


def index(request):
    return render(request, 'main/index.html')


def intro(request):
    return render(request, 'main/about-us.html')


class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = 'main/mypage_detail.html'


def change_password(request):
    context = {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/')
            else:
                messages.error({'error': 'Please correct the error below.'})

    return render(request, 'main/change_password.html', context)
