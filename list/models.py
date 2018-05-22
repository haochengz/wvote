from django.db import models


class EventModel(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    start_date = models.DateField(max_length=30)
    end_date = models.DateField(max_length=30)
    add_time = models.DateField(max_length=30)


class PlayerModel(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    add_time = models.DateField(max_length=30)


class PicsModel(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(max_length=100)
    owner = models.ForeignKey(PlayerModel, on_delete=models.CASCADE)
    add_time = models.DateField(max_length=30)


class VoteModel(models.Model):
    player = models.ForeignKey(PlayerModel, on_delete=models.CASCADE)
    voter = models.CharField(max_length=20)
    add_time = models.DateField(max_length=30)



