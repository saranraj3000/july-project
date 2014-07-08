from django.conf.urls import patterns, include, url
from julyapp import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'julyapp.views.homepage', name='home'),
    url(r'^mainpage$', 'julyapp.views.mainpage', name='new'),
    url(r'^hello$', 'julyapp.views.hello', name='hello'),
    url(r'^hello1$', 'julyapp.views.hello1', name='hello1'),
    url(r'^add$', 'julyapp.views.add', name='add'),
    url(r'^name$', 'julyapp.views.name', name='name'),
    url(r'^list$', 'julyapp.views.list', name='list'),
    url(r'^edit/?(?P<id>\d+?)?/$', 'julyapp.views.edit', name='edit'),
    url(r'^delete/?(?P<id>\d+?)?/$', 'julyapp.views.delete', name='delete'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^adminlogin/', include(admin.site.urls)),
)