from django.db import models

from django.db.models.signals import pre_save

from products.models import Product
from eCommerce.utils import unique_slug_generator


class Tag(models.Model):
    """标签分类"""
    title = models.CharField(max_length=100, verbose_name='标签')
    slug = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

    __repr__ = __str__


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
