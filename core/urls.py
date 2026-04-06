from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import dashboard_view, home_redirect, products_api, register_view

urlpatterns = [
    path("", home_redirect, name="home"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", register_view, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("api/products/", products_api, name="products-api"),
]
