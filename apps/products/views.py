from django.http import Http404
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from .models import Product


class ProductFeaturedListView(ListView):
    """商品特色列表视图"""
    template_name = 'products/list.html'

    def get_queryset(self):
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    """ 商品详情特色视图"""
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    """ 
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()
    """


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


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self, queryset=None):
        request = self.request
        slug = self.kwargs.get("slug")
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhmmm...")
        return instance


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
    # instance = Product.objects.get(pk=pk, featured=True) #id
    # instance = get_object_or_404(Product, pk=pk, featured=True)
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("商品信息不存在")
    context = {'object': instance}
    return render(request, 'products/detail.html', context)
