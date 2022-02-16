from django.contrib import admin
from .models import User, BlogItem, Category
# Register your models here.

admin.site.register(User)
admin.site.register(BlogItem)
admin.site.register(Category)
