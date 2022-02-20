from email.mime import image
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserBioUpdateForm(forms.ModelForm):
    last_name = forms.CharField(required=False, help_text="Optional")
    age = forms.IntegerField(required=False, help_text="Optional")
    address = forms.CharField(required=False, help_text="Optional")
    workplace = forms.CharField(required=False, help_text="Optional")
    image = forms.ImageField(required=False, help_text="Optional")
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'age',
            'address',
            'workplace',
            'bio',
            'image'
        ) 
