from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, Rol

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2', 'first_name')

class RolForm(forms.ModelForm):
    
    class Meta:
        model = Rol
        fields = ("is_regular", "is_agent")