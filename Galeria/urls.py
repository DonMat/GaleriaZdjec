from django.conf.urls import *
from Galeria.views import *

urlpatterns = patterns('',
                       url(r'^$', redirect_log_in),
                       url(r'^log_in/$', log_in),
                       url(r'^auth/$', auth_view),
                       url(r'^log_out/$', log_out),
                       url(r'^register/$', register),
                       url(r'^albums/(?P<user_id>\d+)/$', albums_view),
                       url(r'^albums/(?P<user_id>\d+)/create$', create_album),
                       url(r'^albums/(?P<user_id>\d+)/edit$', main_album_edit),
                       url(r'^albums/(?P<user_id>\d+)/upload$', upload_image),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)$', album_view),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/(?P<image_id>\d+)$', image_view),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/edit$', sub_album_edit),
                       url(r'^albums/(?P<user_id>\d+)/(?P<album_id>\d+)/delete$', sub_album_delete)
)

handler403 = 'Galeria.views.error_403'
handler404 = 'Galeria.views.error_404'
