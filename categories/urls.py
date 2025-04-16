from django.urls import path

from categories.views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
)

urlpatterns = [
    path("list/", CategoryListView.as_view(), name="category_list"),
    path("create/", CategoryCreateView.as_view(), name="category_create"),
    path("<int:pk>/detail/", CategoryDetailView.as_view(), name="category_detail"),
    path("<int:pk>/update/", CategoryUpdateView.as_view(), name="category_update"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
]
