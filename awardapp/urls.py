from django.conf.urls import url,static
from . import views
from  django.conf.urls import url
from django .conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns =[
    url('',views.index,name='index'),
    url('profile/',views.profile,name = 'profile'),
    url(r'^newproject/$',views.new_project,name='newproject'),
    url(r'^search/',views.search_results,name = 'search_results'),
    url('comment/<int:id>/',views.comment,name='comment'),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)