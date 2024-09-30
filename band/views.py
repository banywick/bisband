from django.shortcuts import redirect, render
from band.models import Song, Video, Photo
from .forms import ContactForm

def index(request):
    return render(request, 'band/index.html')

def news(request):
    return render(request, 'band/news.html')

def schedule(request):
    return render(request, 'band/schedule.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Перенаправление на страницу успеха
    else:
        form = ContactForm()

    return render(request, 'band/contact.html', {'form': form})

def photo_gallery(request):
    photos = Photo.objects.all()
    return render(request, 'band/gallery.html', {'photos': photos})

def music(request):
    songs = Song.objects.all()
    return render(request, 'band/music.html', {'songs': songs})

def video(request):
    videos = Video.objects.all()
    return render(request, 'band/video.html', {'videos': videos})

