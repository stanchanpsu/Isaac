from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.profile, name = 'profile'),
url(r'edit/', views.edit, name = 'edit'),

] 
