from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.TextField()

# class BMovie(models.Model):
#     title = models.TextField()
#     audience = models.TextField()
#     poster_url = models.URLField()
#     description = models.TextField()
#     genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_bmovies')

class Movie(models.Model):
    title = models.TextField()
    audience = models.TextField()
    poster_url = models.URLField()
    description = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_movies')

    
class Review(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
