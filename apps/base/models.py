from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField(verbose_name="Estado", default=True)
    created_at = models.DateField(verbose_name="Fecha de creación", auto_now=False, auto_now_add=True)
    updated_at = models.DateField(verbose_name="Fecha de modificación", auto_now=True, auto_now_add=False)
    deleted_at = models.DateField(verbose_name="Fecha de eliminación", auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = "Modelo base"
        verbose_name_plural = "Modelos base"
