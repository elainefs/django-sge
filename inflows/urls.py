from django.urls import path

from inflows.views import (
    InflowCreateListAPIView,
    InflowCreateView,
    InflowDetailView,
    InflowListView,
    InflowRetrieveAPIView,
)

urlpatterns = [
    path("list/", InflowListView.as_view(), name="inflow_list"),
    path("create/", InflowCreateView.as_view(), name="inflow_create"),
    path("<int:pk>/detail/", InflowDetailView.as_view(), name="inflow_detail"),
    path(
        "api/v1/",
        InflowCreateListAPIView.as_view(),
        name="inflow-create-list-api-view"
    ),
    path(
        "api/v1/<int:pk>/",
        InflowRetrieveAPIView.as_view(),
        name="inflow-detail-api-view",
    ),
]
