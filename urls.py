from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gpgauth/', include('django_gpgauth.foo.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
    {'document_root': '/path/to/django_gpgauth/templates/media'}),
    url(r'^captcha/', include('captcha.urls')),
    (r'^$', 'django_gpgauth.views.main'),
    (r'^userinfo/(?P<user_id>\d+)/$', 'django_gpgauth.views.userinfo'),
    (r'^register/$', 'django_gpgauth.gpgauth.views.register'),
    (r'^renew/(?P<username>.*)$', 'django_gpgauth.gpgauth.views.renew'),
    (r'^login/$', 'django_gpgauth.gpgauth.views.login_view'),
    (r'^logout/$', 'django_gpgauth.gpgauth.views.logout_view')
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
