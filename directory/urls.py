from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.directory, name = 'directory'),
url(r'^names', views.names, name = 'names'),
url(r'^ambassador_profile/(?P<ambassador_name>[A-z]+)', views.ambassador_profile, name = 'ambassador_profile'),

]
