from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Product


def home_redirect(request):
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


@login_required
def dashboard_view(request):
    return render(request, "dashboard.html", {"username": request.user.username})


@login_required
def products_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()

    products = Product.objects.all()
    return render(
        request,
        "products.html",
        {
            "form": form,
            "products": products,
            "is_edit": False,
        },
    )


@login_required
def product_edit_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm(instance=product)

    products = Product.objects.all()
    return render(
        request,
        "products.html",
        {
            "form": form,
            "products": products,
            "is_edit": True,
            "editing_product": product,
        },
    )


@login_required
def product_delete_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
    return redirect("products")


@login_required
def products_api(request):
    products = list(
        Product.objects.values("id", "name", "description", "price", "created_at", "updated_at")
    )
    return JsonResponse(products, safe=False)
