from django.conf.urls import *
from Galeria.views import *

urlpatterns = patterns('',
                       url(r'^$', log_in),
                       url(r'^log_in/$', log_in),
                       url(r'^register/$', register),
                       url(r'^album/$', albums_view),
                       url(r'^album/(?P<album_id>\d+)$', album_view),
                       url(r'^album/(?P<album_id>\d+)/(?P<image_id>\d+)$', image_view)
)

handler403 = 'Galeria.views.error_403'
handler404 = 'Galeria.views.error_404'
