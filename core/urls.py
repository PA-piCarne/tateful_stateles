from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    dashboard_view,
    home_redirect,
    product_delete_view,
    product_edit_view,
    products_api,
    products_view,
    register_view,
)

urlpatterns = [
    path("", home_redirect, name="home"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", register_view, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("products/", products_view, name="products"),
    path("products/<int:product_id>/edit/", product_edit_view, name="product-edit"),
    path("products/<int:product_id>/delete/", product_delete_view, name="product-delete"),
    path("api/products/", products_api, name="products-api"),
]
