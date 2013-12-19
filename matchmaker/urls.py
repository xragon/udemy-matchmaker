from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'matchmaker.views.home', name='home'),
    # url(r'^matchmaker/', include('matchmaker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    	'document_root': settings.STATIC_ROOT
    	}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    	'document_root': settings.MEDIA_ROOT
    	}),

    (r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', 'profiles.views.all', name='home'),
    url(r'^members/(?P<username>\w+)/$', 'profiles.views.single_user'),
    url(r'^edit/$', 'profiles.views.edit_profile', name='edit_profile'),
    (r'^edit/job$', 'profiles.views.edit_job'),
    (r'^edit/address$', 'profiles.views.edit_address'),
)
