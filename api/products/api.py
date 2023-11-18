from rest_framework import generics

from api.products.serializers import UnitSizeSerializer, CategorySerializer, DiscountSerializer
from apps.base.api import GenericListApiView
from apps.products.models import UnitSize, Category, Discount


class UnitSizeListApiView(GenericListApiView):
    serializer_class = UnitSizeSerializer


class DiscountListApiView(GenericListApiView):
    serializer_class = DiscountSerializer


class CategoryListApiView(GenericListApiView):
    serializer_class = CategorySerializer
