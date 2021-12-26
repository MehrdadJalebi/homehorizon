
from django.conf.urls import url

from openstack_dashboard.dashboards.kitchen.food import views


urlpatterns = [
    url(r'^$', views.FoodView.as_view(), name='index'),
]
