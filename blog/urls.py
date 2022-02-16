from os import stat
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from base.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('base.urls', namespace='blog')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
