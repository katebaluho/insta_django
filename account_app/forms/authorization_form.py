
from django import forms


class AuthForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)