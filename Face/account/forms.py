from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='re_password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password not match!')
        elif len(cd)>8:
            raise forms.ValidationError('길이가 짧습니다')
        return cd['password2']






