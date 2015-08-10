from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.list_events, name = 'list_events'),
url(r'^(?P<event_id>[0-9]+)/$', views.detail, name = 'detail'),
url(r'^register', views.register, name='register')

]
