from django.conf.urls import patterns, include, url
from studentapp.views import StudentCreate, StudentUpdate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'studentapp.views.index'),
    url(r'^add_student.html/$', 'studentapp.views.add_student'),
    url(r'^addstudent/$', 'studentapp.views.addstudent'),
    url(r'^add_group.html/$', 'studentapp.views.add_group'),
    url(r'index/add_student/$', StudentCreate.as_view(), name='student_add'),
    url(r'index/(?P<pk>\d+)/$', StudentUpdate.as_view(), name='student_update'),
)