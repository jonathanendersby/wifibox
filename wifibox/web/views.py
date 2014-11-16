from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from core.models import Media

def landing(request):
    media = Media.objects.all()    
    return render(request, 'landing.html', {'media':media, })


def about(request):
    return render(request,'about.html')


def info(request, media_id):
    media = Media.objects.get(pk=media_id)
    return render(request, 'info.html', {'m':media, })
