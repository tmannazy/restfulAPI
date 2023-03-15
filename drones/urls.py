from django.urls import re_path

from drones import views

urlpatterns = [
	re_path(r'^drone-categories/$', views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
	re_path(r'^drone-categories/(?P<pk>\d+)$', views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),
	re_path(r'^drones/$', views.DroneList.as_view(), name=views.DroneList.name),
	re_path(r'^drones/(?P<pk>\d+)$', views.DroneDetail.as_view(), name=views.DroneDetail.name),
	re_path(r'^pilots/$', views.PilotList.as_view(), name=views.PilotList.name),
	re_path(r'^pilots/(?P<pk>\d+)$', views.PilotDetail.as_view(), name=views.PilotDetail.name),
	re_path(r'^competitions/$', views.CompetitionList.as_view(), name=views.CompetitionList.name),
	re_path(r'^competitions/(?P<pk>\d+)$', views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
	re_path(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]