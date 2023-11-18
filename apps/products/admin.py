from django.contrib import admin

from apps.products.models import UnitSize, Category, Product, Discount

# Register your models here.
admin.site.register(UnitSize)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Product)
