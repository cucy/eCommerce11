import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, char=string.ascii_lowercase + string.digits):
    """工具函数 随机字符串"""
    return ''.join(random.choice(char) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    这是一个Django项目就假定你的实例有一个模型与塞场和标题字符（char）领域。
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__  # 等价于 Product模型 Product.objects.all()

    qs_exists = Klass.objects.filter(slug=slug).exists()  # 查找模型数据中是否存在 slug
    if qs_exists:
        # 如果存在则重新随机生成
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        # 递归调用
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def unique_order_id_generator(instance):
    """
    this  is for a Django project with an order_id field
    """
    order_new_id = random_string_generator()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id
