from django.db import models
from django.utils import timezone

from utils.images import ImageStorage


class EventModel(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    start_date = models.DateField(max_length=30)
    end_date = models.DateTimeField(max_length=30)
    add_time = models.DateTimeField(default=timezone.now)


class PlayerModel(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=timezone.now)


class PicsModel(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="media/pics/%Y/%m", storage=ImageStorage(), default="media/pics/default.png")
    owner = models.ForeignKey(PlayerModel, on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=timezone.now)


class VoteModel(models.Model):
    player = models.ForeignKey(PlayerModel, on_delete=models.CASCADE)
    voter = models.CharField(max_length=20)
    add_time = models.DateTimeField(default=timezone.now)



