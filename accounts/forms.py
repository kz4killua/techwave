# filepath: /c:/Users/Administrator/Documents/Ontech/Software-Design-and-Analysis/project/techwave/accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)