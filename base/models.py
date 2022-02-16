from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    def __str__(self):
        return self.username


class BlogItem(models.Model):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE) 
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_item_likes')
    dislikes = models.ManyToManyField(User, related_name='blog_item_dislikes')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
