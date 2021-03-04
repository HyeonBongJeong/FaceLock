import json
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .forms import RegisterForm
from .tokens import account_activation_token
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_active = False
            new_user.save()
            current_site = get_current_site(request)
            message = render_to_string('registration/activation_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
            })
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()

            return render(request, 'main/index.html', {'new_user': new_user})
    else:
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form': user_form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('/')
    else:
        return render(request, 'main/index.html', {'error': '계정 활성화 오류'})
    # 포스트 방식 아니면 페이지 띄우기
    return render(request, 'registration/signup.html')


def FindId(request):
    return render(request, 'registration/FindID.html')


def ajax_find_id_view(request):
    email = request.POST.get('email')
    result_id = User.objects.get(email=email)
    # 이메일이 유일하다고 가정함
    print(result_id)
    return HttpResponse(json.dumps({"result_id": str(result_id)}, cls=DjangoJSONEncoder), content_type="application/json")


def FindPwd(request):
    return render(request, 'registration/FindPwd.html')
