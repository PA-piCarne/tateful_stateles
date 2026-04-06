from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import dashboard_view, products_api

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("api/products/", products_api, name="products-api"),
]
