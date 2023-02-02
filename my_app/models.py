from django.db import models

# Create your models here.


class Artist (models.Model):
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    album_url = models.CharField(max_length=100)
    album_cover = models.CharField(max_length=100)

    def __str__(self):
        return self.artist
