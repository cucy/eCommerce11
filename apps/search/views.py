from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):
    template_name = 'search/view.html'

    def get_queryset(self):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)  # method_dict['q']
        if query is not None:
            # return Product.objects.filter(title__icontains=query)
            return Product.objects.search(query)
        return Product.objects.featured()

    def get_context_data(self, **kwargs):
        context = super(SearchProductView, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context
