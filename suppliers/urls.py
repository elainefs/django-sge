from django.urls import path

from suppliers.views import (
    SupplierCreateListAPIView,
    SupplierCreateView,
    SupplierDeleteView,
    SupplierDetailView,
    SupplierListView,
    SupplierRetrieveUpdateDestroyAPIView,
    SupplierUpdateView,
)

urlpatterns = [
    path("list/", SupplierListView.as_view(), name="supplier_list"),
    path("create/", SupplierCreateView.as_view(), name="supplier_create"),
    path("<int:pk>/detail/", SupplierDetailView.as_view(), name="supplier_detail"),
    path("<int:pk>/update/", SupplierUpdateView.as_view(), name="supplier_update"),
    path("<int:pk>/delete/", SupplierDeleteView.as_view(), name="supplier_delete"),
    path(
        "api/v1/",
        SupplierCreateListAPIView.as_view(),
        name="product-create-list-api-view",
    ),
    path(
        "api/v1/<int:pk>/",
        SupplierRetrieveUpdateDestroyAPIView.as_view(),
        name="product-detail-api-view",
    ),
]
