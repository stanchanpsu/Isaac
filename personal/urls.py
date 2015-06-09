from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.profile, name = 'profile'),
url(r'(?P<edit_status>edit)/', views.profile, name = 'profile'),

] 
