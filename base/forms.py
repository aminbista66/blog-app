from dataclasses import field
import django
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import BlogItem

User = get_user_model()

class SignupForm(UserCreationForm):
    last_name = forms.CharField(required=False, help_text="optional")
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class BlogForm(ModelForm):
    image = forms.ImageField(required=False, help_text="optional")
    class Meta:
        model = BlogItem
        fields = (
            'image',
            'title',
            'content',
            'category',
        )
