from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from core.models import Media

def landing(request):
    media = Media.objects.all()    
    return render(request, 'landing.html', {'media':media, })


def about(request):
    return render(request,'about.html')


def serve(request):
    response = HttpResponse()
    response["Content-Disposition"] = "attachment; filename=foo.mp4"
    #response['X-Accel-Redirect'] = "/media/TED Talks/SirKenRobinson_2006.mp4"
    response['X-Sendfile'] = "/media/TED Talks/SirKenRobinson_2006.mp4"
   
    return response


def redir(request):
    return redirect('/media/TED Talks/SirKenRobinson_2006.mp4')
