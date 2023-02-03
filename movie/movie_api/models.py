from django.db import models


class Movie(models.Model):
    movie_title = models.CharField(
        'Title', max_length=255, unique=True, null=False, blank=False
    )
    movie_description = models.TextField(
        'Description', null=True, blank=True
    )
    release_date = models.DateField(
        'Release date', auto_now=False
    )


class Actor(models.Model):
    actor_name = models.CharField(
        'Name', max_length=255, unique=True, null=False, blank=False
    )
    bio = models.TextField(
        'Bio', null=True, blank=True
    )
    actor_photo = models.ImageField


class Genre(models.Model):
    genre = models.CharField(
        'Genre', max_length=64, unique=True, null=False, blank=False
    )
