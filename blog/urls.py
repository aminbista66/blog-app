from os import stat
from unicodedata import name
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from base.forms import UserLoginForm
from base.views import SignupView

class CustomLoginView(LoginView):
    form_class = UserLoginForm


def Landing(request):
    return HttpResponseRedirect(reverse_lazy('blog:home'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Landing),
    path('blog/', include('base.urls', namespace='blog')),
    path('profile/', include('profileapp.urls', namespace='user-profile')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
