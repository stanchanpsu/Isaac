from django.conf.urls import include, url

from . import views

urlpatterns=[

url(r'^$', views.groupme, name = 'groupme'),
url(r'^token', views.token, name ='token'),
url(r'^message', views.message, name = 'message'),
url(r'^group_id', views.group_id, name = 'group_id')

]
