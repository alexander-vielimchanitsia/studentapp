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
    url(r'^$',
        'studentapp.views.students.students_list', name='home'),
    url(r'^students/add/$',
        'studentapp.views.students.add_student'),
    url(r'^students/edit/(?P<student_id>\d+)/$',
        'studentapp.views.students.edit_student'),
    url(r'^students/delete/(?P<student_id>\d+)/$',
        'studentapp.views.students.stud_delete'),
    #GROUP
    url(r'^groups/$',
        'studentapp.views.groups.groups_list', name='group_list'),
    url(r'^groups/add/$',
        'studentapp.views.groups.add_group'),
    url(r'^groups/edit/(?P<group_id>\d+)/$',
        'studentapp.views.groups.edit_group'),
    url(r'^groups/delete/(?P<group_id>\d+)/$',
        'studentapp.views.groups.group_delete'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}))