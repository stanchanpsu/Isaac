from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.list_events, name = 'list_events'),
url(r'^(?P<event_type>outreach)/(?P<event_id>[0-9]+)/$', views.event_detail, name = 'event_detail'),
url(r'^(?P<event_type>tour)/(?P<event_id>[0-9]+)/$', views.event_detail, name = 'event_detail'),

]
