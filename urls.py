from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
#from api.handlers import AdHandler
from cuibono_webservice.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^api/', include('cuibono_webservice.api.urls')),
    url(r'^submit/',include('cuibono_webservice.submit.urls')),
    (r'^$', WelcomeView.as_view()),
    (r'^about/', AboutView.as_view()),
    (r'^team/', TeamView.as_view()),
    (r'^partners/', PartnersView.as_view()),
    (r'^news/', NewsView.as_view()),
    (r'^contact/', ContactView.as_view()),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
)
