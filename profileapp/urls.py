from unicodedata import name
from django.urls import path
from .views import *

app_name = 'profileapp'

urlpatterns = [
    path('', SelfProfileview.as_view(), name="profile-main"),
    path('update/<int:pk>', UpdateBio.as_view(), name='update-bio')
]
