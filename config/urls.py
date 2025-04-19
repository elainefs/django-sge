from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path

from config.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("", home, name="home"),
    path("brands/", include("brands.urls")),
    path("categories/", include("categories.urls")),
    path("suppliers/", include("suppliers.urls")),
    path("inflows/", include("inflows.urls")),
    path("outflows/", include("outflows.urls")),
    path("products/", include("products.urls")),
]
