from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.directory, name = 'directory'),
url(r'names', views.names, name = 'names'),
]
