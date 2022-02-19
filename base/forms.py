from dataclasses import field
from email.mime import image
from logging import PlaceHolder
from tkinter import Widget
from unicodedata import category
import django
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BlogItem, Comment

User = get_user_model()

class UserLoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full bg-gray-800 bg-opacity-40 rounded border border-gray-700 focus:border-indigo-500 focus:bg-gray-900 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full bg-gray-800 bg-opacity-40 rounded border border-gray-700 focus:border-indigo-500 focus:bg-gray-900 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
        'placeholder': 'Password'
    }))
    
class SignupForm(UserCreationForm):
    image = forms.ImageField(required=False, help_text="Optional")
    last_name = forms.CharField(required=False, help_text="optional", widget=forms.TextInput(attrs={
        'class': 'w-full bg-gray-800 bg-opacity-40 rounded border border-gray-700 focus:border-indigo-500 focus:bg-gray-900 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
        'placeholder':'Last Name'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full bg-gray-800 bg-opacity-40 rounded border border-gray-700 focus:border-indigo-500 focus:bg-gray-900 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
        'placeholder':'Username'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full bg-gray-800 bg-opacity-40 rounded border border-gray-700 focus:border-indigo-500 focus:bg-gray-900 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
        'placeholder':'First Name'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full bg-gray-800 bg-opacity-40 rounded border border-gray-700 focus:border-indigo-500 focus:bg-gray-900 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
        'placeholder':'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full bg-gray-800 bg-opacity-40 rounded border border-gray-700 focus:border-indigo-500 focus:bg-gray-900 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
        'placeholder':'Confirm Password'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "w-full bg-gray-800 bg-opacity-40 rounded border border-gray-700 focus:border-indigo-500 focus:bg-gray-900 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out",
        'placeholder':'Email Address'
    }))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'image',
        )

        
class BlogForm(ModelForm):
    image = forms.ImageField(required=False, help_text="Optional", widget=forms.FileInput(attrs={
        'class': '''form-control
    block
    w-full
    px-3
    py-1.5
    text-base
    font-normal
    text-gray-700
    bg-white bg-clip-padding
    border border-solid border-gray-300
    rounded
    transition
    ease-in-out
    m-0
    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none''',
    }))
    class Meta:
        model = BlogItem
        fields = (
            'title',
            'content',
            'category',
            'image',
        )


class CommentForm(ModelForm):
    content = forms.Textarea(attrs={
        'class': '''
        form-control
        block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none''',
    })
    class Meta:
        model = Comment
        fields = (
            'content',
        )
