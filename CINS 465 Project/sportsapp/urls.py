from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'register/$',views.register,name='register'),
    url(r'event/$',views.sport_event,name='event'),
    url(r'team/$', views.sports_team, name='team'),
]
