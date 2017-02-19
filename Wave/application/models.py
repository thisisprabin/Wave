from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=10)
    album_logo = models.FileField(default="File is not avalible")

    def get_absolute_url(self):
        return reverse('music:index')

    def __str__(self):
        return self.album_title+" "+self.artist+" "+self.genre


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    file = models.FileField(default="File is not avalible")

    def get_absolute_url(self):
        return reverse('music:showAlbum', kwargs={'album_id':self.album.id})

    def __str__(self):
        return self.song_title