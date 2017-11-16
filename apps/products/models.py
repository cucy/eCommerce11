from django.db import models


class Product(models.Model):
    """商品模型"""
    title = models.CharField(max_length=120, name='商品名')
    description = models.TextField(name='商品描述')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99, name="商品价格")

    #
    # def __str__(self):
    #     return self.title
    #
    # def __repr__(self):
    #     return self.title

    class Meta:
        verbose_name = '商品模型'
        verbose_name_plural = verbose_name
