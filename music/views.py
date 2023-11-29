from django.shortcuts import render
from django.views.generic import View


def get_base_page(request):
    return render(request, 'base.html')
