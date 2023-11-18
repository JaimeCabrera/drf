from django.urls import path

from api.products.api import UnitSizeListApiView

urlpatterns = [
    path('unit-size/', UnitSizeListApiView.as_view(), name="unit_size")
]
