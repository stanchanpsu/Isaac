from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^events/', include('events.urls', namespace = 'events')),
    url(r'^calendar/', include('cal.urls', namespace = 'cal')),
    
    # index and authetication
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_user, name = 'login'),
    url(r'^logout/', views.logout_user, name = 'logout'),
]
