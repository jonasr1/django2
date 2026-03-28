from django.db import models
from pictures.models import PictureField

from core.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    picture_height = models.PositiveIntegerField(null=True, editable=False)
    picture_width = models.PositiveIntegerField(null=True, editable=False)
    picture = PictureField(
        upload_to="products/",
        width_field="picture_width",
        height_field="picture_height",
    )
    slug = models.SlugField(max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return self.name
