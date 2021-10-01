from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf.urls import url,static
from . import views
from  django.conf.urls import url
from django .conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView



urlpatterns=[
    url(r'^$',views.index,name='index'),
    path('profile/',views.profile,name = 'profile'),
    url(r'^newproject/$',views.new_project,name='newproject'),
    url(r'^search/',views.search_results,name = 'search_results'),
    path('comment/<int:id>/',views.comment,name='comment'),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
    path('rate/<int:id>/',views.rate,name='rates'),
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^api/projects/$',views.ProfileList.as_view()),
    url('profile/',views.profile,name = 'profile'),
    url(r'^newproject/$',views.new_project,name='newproject'),
    url(r'^search/',views.search_results,name = 'search_results'),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
    url('rate/<int:id>/',views.rate,name='rates'),
    url('logout/', LogoutView.as_view(), {"next_page":''}),
   
    
    url(r'^logout/$',views.logout_request,name='logout')
    


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)