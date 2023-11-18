from django.urls import path

from api.products.api import UnitSizeListApiView, DiscountListApiView, CategoryListApiView

urlpatterns = [
    path('unit-size/', UnitSizeListApiView.as_view(), name="unit_size"),
    path('discount/', DiscountListApiView.as_view(), name="discount"),
    path('category/', CategoryListApiView.as_view(), name="category")
]
