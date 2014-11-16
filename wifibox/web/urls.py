from django.conf.urls import patterns, include, url
from django.contrib import admin

from web import views
urlpatterns = patterns('',
    url(r'^$', views.landing, name='landing'),
    url(r'^about/$', views.about, name='about'),
    url(r'^info/(?P<media_id>\d+)/$', views.info, name='info'),
)

