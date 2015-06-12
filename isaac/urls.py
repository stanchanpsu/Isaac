from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^events/', include('events.urls', namespace = 'events')),
    url(r'^calendar/', include('cal.urls', namespace = 'cal')),
    url(r'^directory/', include('directory.urls', namespace = 'directory')),
    url(r'^bc/', include('django_bootstrap_calendar.urls')),
    url(r'^personal/', include('personal.urls', namespace = 'personal')),
    
    # index and authetication
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_user, name = 'login'),
    url(r'^logout/', views.logout_user, name = 'logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
