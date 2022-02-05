from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Password'}))
