from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='UserFormView'),
    url(r'album/(?P<album_id>[0-9]+)/delete$', views.deleteAlbum, name='deleteAlbum'),
    url(r'album/(?P<pk>[0-9]+)/update$', views.AlbumUpdate.as_view(), name='updateAlbum'),
    url(r'^(?P<album_id>[0-9]+)$', views.showAlbum, name='showAlbum'),
    url(r'^album/new/$', views.AlbumCreate.as_view(), name='AlbumCreate'),
    url(r'song/(?P<song_id>[0-9]+)/add/$', views.AddNewSong.as_view(), name='AddNewSong'),
    url(r'song/(?P<pk>[0-9]+)/edit/$', views.SongUpdate.as_view(), name='edit'),
    url(r'song/(?P<album_id>[0-9]+)/delete/(?P<song_id>[0-9]+)$', views.deleteSong, name='deleteSong'),
]