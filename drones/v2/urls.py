from django.urls import re_path

from drones import views
from drones.v2 import views as views_v2

urlpatterns = [
	re_path(r'^vehicle-categories/$', views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
	re_path(r'^vehicle-categories/(?P<pk>\d)$', views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),
	re_path(r'^vehicles/$', views.DroneList.as_view(), name=views.DroneList.name),
	re_path(r'^vehicles/(?P<pk>\d+)$', views.DroneDetail.as_view(), name=views.DroneDetail.name),
	re_path(r'^pilots/$', views.PilotList.as_view(), name=views.PilotList.name),
	re_path(r'^pilots/(?P<pk>\d+)$', views.PilotDetail.as_view(), name=views.PilotDetail.name),
	re_path(r'^competitions/$', views.CompetitionList.as_view(), name=views.CompetitionList.name),
	re_path(r'^competitions/(?P<pk>\d+)$', views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
	re_path(r'^$', views_v2.ApiRootVersion2.as_view(), name=views_v2.ApiRootVersion2.name),
]
