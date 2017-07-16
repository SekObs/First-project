from django.conf.urls import url
from django.http import HttpResponse

from blog import views

urlpatterns = [
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
]
