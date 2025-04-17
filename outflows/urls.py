from django.urls import path

from outflows.views import OutflowCreateView, OutflowDetailView, OutflowListView

urlpatterns = [
    path("list/", OutflowListView.as_view(), name="outflow_list"),
    path("create/", OutflowCreateView.as_view(), name="outflow_create"),
    path("<int:pk>/detail/", OutflowDetailView.as_view(), name="outflow_detail"),
]
