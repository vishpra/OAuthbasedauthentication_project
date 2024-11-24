from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  # Use 'User' if not using a custom user model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Use 'User' if not using a custom user model
        fields = ('username', 'email', 'password1', 'password2', 'phone_number')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Use 'User' if not using a custom user model
        fields = ('username', 'password')
