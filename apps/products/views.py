from django.http import Http404
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    """商品列表"""
    # queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
    """商品详情视图"""
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        print(context)
        return context

    def get_object(self, queryset=None):
        request = self.request
        pk = self.kwargs.get('pk')
        instace = Product.objects.get_by_id(pk)
        if instace is None:
            raise Http404("商品不存在")
        return instace


def product_detail_view(request, pk=None, *args, **kwargs):
    """
    qs = Product.objects.filter(id=pk)
    context = {}
    if qs.exists() and qs.count() == 1:
        instanceobj = qs.first()
    else:
        Http404("商品信息不存在")
    context["object"] = instanceobj
    """
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("商品信息不存在")
    context = {'object': instance}
    return render(request, 'products/detail.html', context)
