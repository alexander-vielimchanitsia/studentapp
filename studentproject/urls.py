from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    #ADMIN
    url(r'^admin/', include(admin.site.urls)),

    #STUDENT
    url(r'^$', 'studentapp.views.students.index', name='home'),
    url(r'^addstudent/$', 'studentapp.views.students.addstudent'),
    url(r'^edit_student/(?P<student_id>\d+)/$', 'studentapp.views.students.edit_student'),
    url(r'^stud_delete/(?P<student_id>\d+)/$', 'studentapp.views.students.stud_delete'),
    #GROUP
    url(r'^groups/$', 'studentapp.views.groups.groups'),
    url(r'^groups/addgroup/$', 'studentapp.views.groups.addgroup'),
    url(r'^groups/edit_group/(?P<group_id>\d+)/$', 'studentapp.views.groups.edit_group'),
    url(r'^groups/group_delete/(?P<group_id>\d+)/$', 'studentapp.views.groups.group_delete'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))