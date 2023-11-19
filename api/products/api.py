from rest_framework import generics, status, serializers
from rest_framework.response import Response

from api.products.serializers import UnitSizeSerializer, CategorySerializer, DiscountSerializer, ProductSerializer
from apps.base.api import GenericListApiView


class UnitSizeListApiView(GenericListApiView):
    serializer_class = UnitSizeSerializer


class DiscountListApiView(GenericListApiView):
    serializer_class = DiscountSerializer


class CategoryListApiView(GenericListApiView):
    serializer_class = CategorySerializer


# products api

class ProductListApiView(GenericListApiView):
    serializer_class = ProductSerializer


class ProductCreateApiView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Producto agregado corectamente"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    # se puede reescribir con el metodo get
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        # Aquí puedes realizar cualquier lógica adicional antes o después de obtener el objeto.
        print(kwargs["pk"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProductDestroyApiView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Validar el objeto
        if not instance.is_valid():
            return Response({"msg":"No existe el item"}, status=status.HTTP_204_NO_CONTENT)
        # procesar el obj s
        instance.state = False
        instance.save()
        return Response({"msg": "Producto eliminado"},status=status.HTTP_200_OK)


class ProductUpdateApiView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def patch(self, request, *args, **kwargs):
        if kwargs["pk"]:
            instance = self.get_object()
