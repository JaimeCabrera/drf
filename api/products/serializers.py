from rest_framework import serializers

from apps.products.models import UnitSize, Category, Discount, Product


# general serializers
class UnitSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitSize
        exclude = ("state",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("state",)


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ("state",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("state",)
