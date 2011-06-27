from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
	(r'^$', 'splash.views.createEntry'),
	(r'^success/', 'splash.views.success'),
	(r'^about/', 'splash.views.about'),
	(r'^team/', 'splash.views.team'),
	(r'^contact/', 'splash.views.contact'),
	
	
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root': '/Users/rikuseppala/Development/unprob/media'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

