from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(ModelForm):
        password = forms.CharField(min_length=6, max_length=255,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                   label="Nouveau mot de passe")

        class Meta:
            model = User
            fields = ['username', 'email', 'password']
            widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'})}
