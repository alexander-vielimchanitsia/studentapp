from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'studentapp.views.index'),
    url(r'^add_student.html/', 'studentapp.views.add_student'),
    url(r'^add_group.html/', 'studentapp.views.add_group'),
)