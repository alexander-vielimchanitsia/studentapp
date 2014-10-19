from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('studentapp.urls')),
    url(r'^index/', include('studentapp.urls')),
    url(r'^page/(\d+)/$', 'studentapp.views.index'),
    url(r'groups/$', 'studentapp.views.groups'),
    url(r'^groups/page/(\d+)/$', 'studentapp.views.groups'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))