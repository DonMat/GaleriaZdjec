from django.conf.urls import *
from Galeria.views import *

urlpatterns = patterns('',
                       url(r'^$', redirect_log_in),
                       url(r'^log_in/$', auth_view),
                       url(r'^log_out/$', log_out),
                       url(r'^register/$', register),
                       url(r'^search/', search),
                       url(r'^albums/(?P<user_id>\d+)/$', main_album),
                       url(r'^albums/(?P<user_id>\d+)/create$', sub_album_create),
                       url(r'^albums/(?P<user_id>\d+)/edit$', main_album_edit),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/$', sub_album_view),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/upload$$', image_upload),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/edit$', sub_album_edit),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/delete$', sub_album_delete),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/(?P<image_id>\d+)/$', image_view),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/(?P<image_id>\d+)/add_comment$', add_comment),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/(?P<image_id>\d+)/edit$', image_edit),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/(?P<image_id>\d+)/delete$', image_delete),
)

handler403 = 'Galeria.views.error_403'
handler404 = 'Galeria.views.error_404'
