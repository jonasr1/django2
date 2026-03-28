from django.contrib import admin

from django2.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "stock",
        "slug",
        "created_at",
        "updated_at",
        "is_active",
    )
