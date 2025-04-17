from django.urls import path

from inflows.views import (
    InflowCreateView,
    InflowDetailView,
    InflowListView,
)

urlpatterns = [
    path("list/", InflowListView.as_view(), name="inflow_list"),
    path("create/", InflowCreateView.as_view(), name="inflow_create"),
    path("<int:pk>/detail/", InflowDetailView.as_view(), name="inflow_detail"),
]
