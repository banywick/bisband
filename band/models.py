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



class Photo(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/', verbose_name='Фото')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return ''if self.title is None else self.title
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии' 
        ordering = ['order']


class Application(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')  
    email = models.EmailField(verbose_name='Почта')   
    text = models.TextField(verbose_name='Текст')

    def __str__(self) -> str:
        return f'{self.name}'  
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки' 



class Concert(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='concert_images/', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата и время')
    link = models.URLField(null=True, blank=True, verbose_name='Ссылка на мероприятие')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты' 


from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='news_images/', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

