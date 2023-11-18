from rest_framework import generics

from api.products.serializers import UnitSizeSerializer
from apps.products.models import UnitSize


class UnitSizeListApiView(generics.ListAPIView):
    serializer_class = UnitSizeSerializer

    def get_queryset(self):
        return UnitSize.objects.filter(state=True)
