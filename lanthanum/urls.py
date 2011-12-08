from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template

if 'admin_tools' in settings.INSTALLED_APPS:
    import admin_tools
from os.path import dirname, abspath, join
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^account/login', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^account/logout', 'django.contrib.auth.views.logout', {'template_name':'logout.html'}, name='logout'),
    url(r'^account/', include('django.contrib.auth.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^$', direct_to_template, {'template':'home.html'})
)


if 'admin_tools' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^admin_tools/', include('admin_tools.urls')), 
        (r'^'+settings.MEDIA_URL[1:]+r'admin_tools/(?P<path>.*)$', 'django.views.static.serve',
                     {'document_root': join(dirname(abspath(admin_tools.__file__)), 'media/admin_tools')} ),
    ]

if 'markitup' in settings.INSTALLED_APPS:
    urlpatterns += [ url(r'^markitup/', include('markitup.urls')) ]

if 'LanConnect.tournaments' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^tournaments/', include('LanConnect.joust.urls')), 
        url(r'^$', lambda request: redirect('/tournaments/')), ]

if 'LanConnect.jquery' in settings.INSTALLED_APPS:
    urlpatterns += [ url(r'^jquery/', include('LanConnect.jquery.urls', namespace = 'jquery')), ]

if settings.DEBUG:
    urlpatterns += [
        url(r'^'+settings.MEDIA_URL[1:]+r'(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT} ),
    ]
