from django.conf.urls import include, url

from . import views

urlpatterns=[url(r'^$', views.index, name = "index"),url(r'^register/', views.register, name = 'register'),url(r'^logout/', views.logout_user, name = 'logout'),]
