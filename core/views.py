from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render


@login_required
def dashboard_view(request):
    return render(request, "dashboard.html", {"username": request.user.username})


def products_api(request):
    products = [
        {"name": "Laptop", "price": 1200},
        {"name": "Mouse", "price": 25},
    ]
    return JsonResponse(products, safe=False)
