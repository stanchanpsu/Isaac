from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.groupme, name = 'groupme'),
url(r'^token', views.token, name ='token'),
url(r'^message', views.message, name = 'message'),
url(r'^group_id', views.group_id, name = 'group_id'),
url(r'^event/(?P<group_id>[0-9]+)/$', views.event_call, name="event_call"),
url(r'^create/(?P<event_id>[0-9]+)', views.event_create, name="event_create"),

]
