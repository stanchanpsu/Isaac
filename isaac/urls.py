from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'isaac.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^events/', include('events.urls')),
    
    # index and authetication
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_user, name = 'login'),
    url(r'^logout/', views.logout_user, name = 'logout'),
]
