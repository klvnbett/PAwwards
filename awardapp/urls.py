from django.conf.urls import url
from . import views
from  django.conf.urls import url
from django .conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns =[
    url('^$',views.index,name='index'),

]