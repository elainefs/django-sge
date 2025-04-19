from django.urls import path

from categories.views import (
    CategoryCreateListAPIView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryRetrieveUpdateDestroyAPIView,
    CategoryUpdateView,
)

urlpatterns = [
    path("list/", CategoryListView.as_view(), name="category_list"),
    path("create/", CategoryCreateView.as_view(), name="category_create"),
    path("<int:pk>/detail/", CategoryDetailView.as_view(), name="category_detail"),
    path("<int:pk>/update/", CategoryUpdateView.as_view(), name="category_update"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
    path(
        "api/v1/",
        CategoryCreateListAPIView.as_view(),
        name="category-create-list-api-view",
    ),
    path(
        "api/v1/<int:pk>/",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category-detail-api-view",
    ),
]
