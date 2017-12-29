
#add_to_end: 2017-08-21 12:42:07.565864
from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^box/', views.bad_boxes, name='bad_boxes'),
	url(r'^login/', views.login, name='login'),
	url(r'^create/', views.create, name='create'),
	url(r'^join/', views.join, name='join'),
	url(r'^wait/(?P<pk>\d+)$', views.wait, name='wait'),
	url(r'^game2_play/', views.game2_play, name='game2_play'),
	url(r'^game2_end/', views.game2_end, name='game2_end'),
	url(r'^$', views.home, name='home'),
	url(r'^iq/', views.iq, name='iq'),
	url(r'^iq_end/', views.iq_end, name='iq_end'),
]
#add_to_end: 2017-08-21 12:42:07.565902
