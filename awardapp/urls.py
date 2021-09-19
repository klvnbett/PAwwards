from django.conf.urls import url,static
from . import views
from  django.conf.urls import url
from django .conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns =[
    url('',views.index,name='index'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)