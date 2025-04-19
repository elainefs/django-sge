from django.urls import path

from products.views import (
    ProductCreateListAPIView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductRetrieveUpdateDestroyAPIView,
    ProductUpdateView,
)

urlpatterns = [
    path("list/", ProductListView.as_view(), name="product_list"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/detail/", ProductDetailView.as_view(), name="product_detail"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "api/v1/",
        ProductCreateListAPIView.as_view(),
        name="product-create-list-api-view",
    ),
    path(
        "api/v1/<int:pk>/",
        ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="product-detail-api-view",
    ),
]
