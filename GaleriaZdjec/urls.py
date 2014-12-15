from django.conf.urls import patterns, include, url
from django.contrib import admin
import Galeria.urls
from django.http import HttpResponse, HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GaleriaZdjec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(Galeria.urls)), #    include(admin.site.urls)),
    url(r'^site/', include(Galeria.urls)),
    url(r'^$', include(Galeria.urls))   #routing gdy wpiszemy sam adres
)
