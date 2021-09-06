from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=50)
    pics = models.ImageField(upload_to='pics')
    category = models.PositiveSmallIntegerField(unique=True)


class Game_log(models.Model):
    topic = models.CharField(max_length=50)
    level = models.CharField(max_length=7)
    user_id = models.PositiveIntegerField()
    datetime = models.CharField(max_length=14, default='N/A')
    score = models.PositiveIntegerField()
