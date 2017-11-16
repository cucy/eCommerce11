from django.shortcuts import render

from django.views.generic import ListView

from .models import Product


class ProductView(ListView):
    """商品列表"""
    queryset = Product.objects.all()
    template_name = 'products/list.html'


def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(request, 'products/list.html', context)
