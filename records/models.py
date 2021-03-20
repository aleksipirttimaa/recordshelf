from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Record(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)

    def __str__(self):
        return self.name



class Possession(models.Model):
    record = models.ForeignKey(Record, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
