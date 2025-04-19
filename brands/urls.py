from django.urls import path

from brands.views import (
    BrandCreateListAPIView,
    BrandCreateView,
    BrandDeleteView,
    BrandDetailView,
    BrandListView,
    BrandRetrieveUpdateDestroyAPIView,
    BrandUpdateView,
)

urlpatterns = [
    path("list/", BrandListView.as_view(), name="brand_list"),
    path("create/", BrandCreateView.as_view(), name="brand_create"),
    path("<int:pk>/detail/", BrandDetailView.as_view(), name="brand_detail"),
    path("<int:pk>/update/", BrandUpdateView.as_view(), name="brand_update"),
    path("<int:pk>/delete/", BrandDeleteView.as_view(), name="brand_delete"),
    path(
        "api/v1/",
        BrandCreateListAPIView.as_view(),
        name="brand-create-list-api-view",
    ),
    path(
        "api/v1/<int:pk>/",
        BrandRetrieveUpdateDestroyAPIView.as_view(),
        name="brand-detail-api-view",
    ),
]
