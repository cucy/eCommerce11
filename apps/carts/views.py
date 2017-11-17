from django.shortcuts import render

from .models import Cart


def cart_home(request):
    cart_onj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {})
