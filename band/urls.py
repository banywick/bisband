from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('schedule/', views.schedule, name='schedule'),
    path('gallery/', views.photo_gallery, name='gallery'),
    path('music/', views.music, name='music'),
    path('video/', views.video, name='video'),
]
