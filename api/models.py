from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class Genre(models.Model):
    name = models.TextField(primary_key=True, max_length=200)


class Movie(models.Model):
    title = models.TextField()
    image = models.URLField(max_length=500)
    genres = models.ManyToManyField(Genre, related_name='genres', null=True)
    description = models.TextField(default='No description')
    released = models.CharField(max_length=10)
    raiting = models.FloatField(default=0)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    favorite = models.ManyToManyField(Movie,related_name="favorite",null=True,blank=True)

class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text
