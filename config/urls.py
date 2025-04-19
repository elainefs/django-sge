from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from config.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("authentication.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", home, name="home"),
    path("brands/", include("brands.urls")),
    path("categories/", include("categories.urls")),
    path("suppliers/", include("suppliers.urls")),
    path("inflows/", include("inflows.urls")),
    path("outflows/", include("outflows.urls")),
    path("products/", include("products.urls")),
]
