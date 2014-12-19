from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	url(r'^$', views.MyView.as_view(), name='index'),
)

