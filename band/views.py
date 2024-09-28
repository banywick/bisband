from django.shortcuts import render
from band.models import Song, Video

def index(request):
    return render(request, 'band/index.html')

def news(request):
    return render(request, 'band/news.html')

def schedule(request):
    return render(request, 'band/schedule.html')

def contact(request):
    return render(request, 'band/contact.html')

def photo_gallery(request):
    return render(request, 'band/gallery.html')

def music(request):
    songs = Song.objects.all()
    return render(request, 'band/music.html', {'songs': songs})

def video(request):
    videos = Video.objects.all()
    return render(request, 'band/video.html', {'videos': videos})

