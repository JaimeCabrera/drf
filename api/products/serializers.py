from rest_framework import serializers

from apps.products.models import UnitSize, Category, Discount, Product


# general serializers
class UnitSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitSize
        exclude = ("state", "created_at", "updated_at", "deleted_at")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("state", "created_at", "updated_at", "deleted_at")


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ("state", "created_at", "updated_at", "deleted_at")


class ProductSerializer(serializers.ModelSerializer):
    # forma 1
    # unit_size = UnitSizeSerializer()
    # category = CategorySerializer()
    # forma 2 usando clase meta
    # unit_size = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()
    # 3ra forma con el to reprensentation

    class Meta:
        model = Product
        exclude = ("state", "created_at", "updated_at", "deleted_at")

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'unit_size': instance.unit_size.description,
            'category': instance.category.name,
            'stock': instance.stock,
            'image': instance.image if instance.image != '' else '',
        }
