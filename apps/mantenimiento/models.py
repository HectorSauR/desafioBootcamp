from django.db import models

from apps.auto.models import Auto
# Create your models here.


class Mantenimiento(models.Model):

    auto = models.ForeignKey(Auto, verbose_name="Auto que esta en mantenimiento",
                             on_delete=models.CASCADE, related_name="auto")
    kilometraje = models.FloatField(
        verbose_name="Cantidad de Kilometros")
    descripcion = models.CharField(
        max_length=50, verbose_name="Descripcion Mantenimiento")
    costo = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Costo del Mantenimiento")
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return 'Mantenimiento %s al auto %s' % (self.descripcion, self.auto)
