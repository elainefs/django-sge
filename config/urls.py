from django.contrib import admin
from django.urls import include, path

from config.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("brands/", include("brands.urls")),
    path("categories/", include("categories.urls")),
    path("suppliers/", include("suppliers.urls")),
    path("inflows/", include("inflows.urls")),
    path("outflows/", include("outflows.urls")),
    path("products/", include("products.urls")),
]
