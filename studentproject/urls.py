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
    #url(r'^index/?message=addstudent_message/', view='studentapp.views.addstudent' name='addstudent_message'),
    url(r'^page/(\d+)/$', 'studentapp.views.index'),
    url(r'^groups/$', 'studentapp.views.groups'),
    url(r'^groups/addgroup/$', 'studentapp.views.addgroup'),
    url(r'^groups/page/(\d+)/$', 'studentapp.views.groups'),
    url(r'^edit_student/(?P<student_id>\d+)/$', 'studentapp.views.edit_student'),
    url(r'^groups/edit_group/(?P<group_id>\d+)/$', 'studentapp.views.edit_group'),
    url(r'^stud_delete/(?P<student_id>\d+)/$', 'studentapp.views.stud_delete'),
    url(r'^groups/group_delete/(?P<group_id>\d+)/$', 'studentapp.views.group_delete'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))