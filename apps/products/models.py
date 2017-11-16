import os
import random

from django.db import models


def get_filename_ext(filepath):
    """获取文件名和扩展名函数"""
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    """生成新的文件扩展名"""
    new_filename = random.randint(1, 2345623456)
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class ProductManager(models.Manager):
    """商品模型管理器"""

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    """商品模型"""
    title = models.CharField(max_length=120, verbose_name="商品名")
    description = models.TextField(verbose_name='商品描述')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99, verbose_name="商品价格")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = '商品模型'
        verbose_name_plural = verbose_name

    objects = ProductManager()
