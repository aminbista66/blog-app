from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

class User(AbstractUser):
    image = models.ImageField(null=True, upload_to="profile_image/")
    def __str__(self):
        return self.username


class BlogItem(models.Model):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE) 
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(max_length=255)
    # content = models.TextField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_item_likes')
    dislikes = models.ManyToManyField(User, related_name='blog_item_dislikes')
    views = models.ManyToManyField(User, related_name="blog_views")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogItem, related_name="comments", on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
