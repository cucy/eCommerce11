from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from .models import Product


class ProductView(ListView):
    """商品列表"""
    queryset = Product.objects.all()
    template_name = 'products/list.html'


def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
    """商品详情视图"""
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        print(context)
        return context


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = get_object_or_404(Product, pk=pk)
    context = {'object': instance}
    return render(request, 'products/detail.html', context)
