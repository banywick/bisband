from ast import mod
from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка' 