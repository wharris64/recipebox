from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    biosection = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('Recipe', related_name='fave')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    description = models.TextField()
    timerequired = models.IntegerField()
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"
