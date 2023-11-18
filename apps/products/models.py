from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel


# Create your models here.
class Unitsize(BaseModel):
    description = models.CharField(verbose_name="Descripcion", max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medida"

    def __str__(self):
        return self.description


class Category(BaseModel):
    name = models.CharField(verbose_name="Nombre de la categoria", max_length=50, blank=False, null=False, unique=True)
    unit_size = models.ForeignKey(Unitsize, verbose_name="Unidad de medida", related_name="category_unitsize",
                                  on_delete=models.PROTECT)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Caytegorias"

    def __str__(self):
        return self.name


class Discount(BaseModel):
    discount = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Categoria",
                                 related_name="discount_category")
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Descuento"
        verbose_name_plural = "Descuentos"

    def __str__(self):
        return f"{self.discount} {self.category}"


class Product(BaseModel):
    name = models.CharField(verbose_name="Nombre del producto", max_length=150,
                            unique=True, blank=False, null=False)
    description = models.TextField(verbose_name="Descripción del producto", blank=False, null=False)
    stock = models.IntegerField(verbose_name="Stock",)
    image = models.ImageField(verbose_name="Imagen", upload_to="products/", blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.name}"
