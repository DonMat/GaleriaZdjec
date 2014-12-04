from django.conf.urls import *
from Galeria.views import *

urlpatterns = patterns('',
                       url(r'^$', log_in),
                       url(r'log_in/$', log_in),
                       url(r'register/$', register),
                       url(r'albums/$', albums_view)
)