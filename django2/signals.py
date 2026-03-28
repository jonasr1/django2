from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from django2.models import Product


@receiver(pre_save, sender=Product)
def create_slug_product(instance: Product, **kwargs) -> None:
    instance.slug = slugify(instance.name)
