from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from studentapp.views.students import StudentDeleteView
from studentapp.views.groups import GroupDeleteView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #ADMIN
    url(r'^admin/', include(admin.site.urls)),
    #ACCOUNTS
    url(r'^accounts/logout/$',
        'studentapp.views.accounts.logout_view', name='auth_logout'),
    url(r'^accounts/login/$',
        'studentapp.views.accounts.login_view', name='auth_login'),
    url(r'^accounts/register/$',
        'studentapp.views.accounts.registration_view', name='auth_register'),
    #STUDENT
    url(r'^$',
        'studentapp.views.students.students_list', name='home'),
    url(r'^students/add/$',
        'studentapp.views.students.add_student', name='add_student'),
    url(r'^students/edit/(?P<student_id>\d+)/$',
        'studentapp.views.students.edit_student', name='edit_student'),
    url(r'^students/delete/(?P<pk>\d+)/$',
        StudentDeleteView.as_view(), name='delete_student'),
    #GROUP
    url(r'^groups/$',
        'studentapp.views.groups.groups_list', name='group_list'),
    url(r'^groups/add/$',
        'studentapp.views.groups.add_group', name='add_group'),
    url(r'^groups/edit/(?P<group_id>\d+)/$',
        'studentapp.views.groups.edit_group', name='edit_group'),
    url(r'^groups/delete/(?P<pk>\d+)/$',
        GroupDeleteView.as_view(), name='delete_group'),
)

# if settings.DEBUG:
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}))
