from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from .views import home_page, about_page, contact_page, login_page, register_page

from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view, \
    ProductFeaturedListView, ProductFeaturedDetailView

urlpatterns = [
    url(r'^$', home_page, name='index'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact_page'),
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),

    url(r'^products/$', ProductListView.as_view()),
    url(r'^products-fbv/$', product_list_view),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
