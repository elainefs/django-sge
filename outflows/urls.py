from django.urls import path

from outflows.views import (
    OutflowCreateListAPIView,
    OutflowCreateView,
    OutflowDetailView,
    OutflowListView,
    OutflowRetrieveAPIView,
)

urlpatterns = [
    path("list/", OutflowListView.as_view(), name="outflow_list"),
    path("create/", OutflowCreateView.as_view(), name="outflow_create"),
    path("<int:pk>/detail/", OutflowDetailView.as_view(), name="outflow_detail"),
    path(
        "api/v1/",
        OutflowCreateListAPIView.as_view(),
        name="outflow-create-list-api-view",
    ),
    path(
        "api/v1/<int:pk>/",
        OutflowRetrieveAPIView.as_view(),
        name="outflow-detail-api-view",
    ),
]
