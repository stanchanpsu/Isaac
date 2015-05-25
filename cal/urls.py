from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.month, name = 'calendar'),
url(r'^(?P<year>[0-9]{4})/(?P<month>[1-9]{1,2})$', views.month, )

]
