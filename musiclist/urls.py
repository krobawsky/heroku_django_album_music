from django.conf.urls import url

from musiclist import views

urlpatterns = [
    url(r'^albums/$', views.album_list),
    url(r'^tracks/$', views.track_list),
    url(r'^tracks/(?P<pk>[0-9]+)/$', views.track_detail),
]