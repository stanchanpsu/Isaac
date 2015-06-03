from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.month, name = 'calendar'),
url(r'^year$', views.year, name = 'current_year'),
url(r'^(?P<year>[0-9]{4})$', views.year, name = "year"),
url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})$', views.month, name = "month")

]
