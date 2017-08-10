from django.conf.urls import url

from ticket import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.ticket_listing, name="listing")
]
