from django.urls import re_path
from careerJournal import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    re_path(r'^user$', views.usersApi),
    re_path(r'^user/([0-9]+)$', views.usersApi),
    
    re_path(r'^employee$', views.employmentApi),
    re_path(r'^employee/([0-9]+)$', views.employmentApi),
    
    re_path(r'^employee/savefile', views.saveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)