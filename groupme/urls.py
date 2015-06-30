from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.groupme, name = 'groupme'),
url(r'^token', views.token, name ='token'),
url(r'^getgroups', views.getGroups, name = 'getGroups'),

]
