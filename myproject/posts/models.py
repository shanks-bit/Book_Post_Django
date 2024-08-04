from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField()
    genre = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_recommendations')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
