import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# class EnquiriesForm(forms.Form):
#     subject = forms.CharField(label="subject",max_length=100)
#     name = forms.CharField(label="name",max_length=100)
#     email = forms.CharField(label="email",max_length=100)
#     message = forms.CharField(label="message",max_length=100)


class LoginForm(forms.Form):
    email = forms.CharField(label="email",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    fullname = forms.CharField(label="fullname",max_length=100)
    email = forms.CharField(label="email",max_length=100)
    password = forms.CharField(label="password",max_length=100)
    confirm_password = forms.CharField(label="confirm_password", max_length=100)
