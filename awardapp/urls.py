from django.conf.urls import url,static
from . import views
from  django.conf.urls import url
from django .conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns =[
    url(r'^$',views.index,name='index'),
    url('profile/',views.profile,name = 'profile'),
    url(r'^newproject/$',views.new_project,name='newproject'),
    url(r'^search/',views.search_results,name = 'search_results'),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
    url('rate/<int:id>/',views.rate,name='rates'),
    url('logout/', LogoutView.as_view(), {"next_page":''}),
    url(r'^api/projectview/$', views.ProjectApi.as_view()),
    url(r'^api/profilesview/$', views.ProfileApi.as_view()),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)