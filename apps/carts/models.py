from django.db import models
from django.conf import settings

from products.models import Product

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    """购物车"""
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='用户名')
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2, verbose_name='总价')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
