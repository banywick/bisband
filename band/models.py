from ast import mod
from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    audio_file = models.FileField(upload_to='music/', verbose_name='Аудио файл')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка' 


class Video(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    youtube_url = models.CharField(max_length=50, verbose_name='ID Видео')

    def __str__(self):
        return self.youtube_url
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео' 