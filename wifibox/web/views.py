from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from django.http import HttpResponse

from core.models import Media, MediaCategory

def landing(request):
    media = Media.objects.all().order_by('-added')[:10]    
    return render(request, 'landing.html', {'media':media, })


def about(request):
    return render(request,'about.html')


def info(request, media_id):
    media = Media.objects.get(pk=media_id)
    return render(request, 'info.html', {'m':media, })


def browse(request):
    cats = MediaCategory.objects.annotate(num=Count('media')).order_by('name')
    
    if request.GET.get('category'):
        category = request.GET.get('category')
        media = Media.objects.filter(category__name=category)
        return render(request, 'browse.html', {'cats': cats, 'media': media, 'category':category })

    return render(request, 'browse.html', {'cats': cats, })
