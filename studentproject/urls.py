from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from studentapp.views.students import StudentDeleteView
from studentapp.views.groups import GroupDeleteView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # accounts
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name='auth_logout'),
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'},
        name='auth_login'),
    url(r'^accounts/register/$',
        CreateView.as_view(
            template_name='accounts/register.html',
            form_class=UserCreationForm,
            success_url='/',
        ),
        name='auth_register'),

    # students
    url(r'^$',
        'studentapp.views.students.students_list', name='home'),
    url(r'^students/add/$',
        'studentapp.views.students.add_student', name='add_student'),
    url(r'^students/edit/(?P<pk>\d+)/$',
        'studentapp.views.students.edit_student', name='edit_student'),
    url(r'^students/delete/(?P<pk>\d+)/$',
        StudentDeleteView.as_view(), name='delete_student'),

    # groups
    url(r'^groups/$',
        'studentapp.views.groups.groups_list', name='group_list'),
    url(r'^groups/add/$',
        'studentapp.views.groups.add_group', name='add_group'),
    url(r'^groups/edit/(?P<pk>\d+)/$',
        'studentapp.views.groups.edit_group', name='edit_group'),
    url(r'^groups/delete/(?P<pk>\d+)/$',
        GroupDeleteView.as_view(), name='delete_group'),
)

# if settings.DEBUG:
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}))
