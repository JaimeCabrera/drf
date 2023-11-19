from django.urls import path

from api.products.api import UnitSizeListApiView, DiscountListApiView, CategoryListApiView, ProductListApiView, \
    ProductCreateApiView, ProductDetailApiView, ProductDestroyApiView

urlpatterns = [
    path('unit-size/', UnitSizeListApiView.as_view(), name="unit_size"),
    path('discount/', DiscountListApiView.as_view(), name="discount"),
    path('category/', CategoryListApiView.as_view(), name="category"),
    path('product/list', ProductListApiView.as_view(), name="product"),
    path('product/create', ProductCreateApiView.as_view(), name="product_create"),
    path('product/detail/<int:pk>', ProductDetailApiView.as_view(), name="product_detail"),
    path('product/destroy/<int:pk>', ProductDestroyApiView.as_view(), name="product_destroy")
]
