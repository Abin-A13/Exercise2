from email.policy import default
from random import choices
from django.db import models
from django.conf import settings
from .enums import GenreType


class Book(models.Model):
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="author")
    genre = models.CharField(max_length=50,choices=GenreType.choices(),default=GenreType.LITERARY)
    review = models.PositiveIntegerField()
    favorite = models.BooleanField()

    def __str__(self):
        return self.title
