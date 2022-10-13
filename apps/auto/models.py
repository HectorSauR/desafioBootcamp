from django.db import models

from apps.user.models import User
from apps.modelo.models import Modelo
# Create your models here.

class Auto (models.Model):

    placa = models.CharField(max_length=6,verbose_name="Placas del auto")
    kilometraje = models.FloatField(verbose_name="Kilometraje actual del auto")
    cliente = models.ForeignKey(User,verbose_name="Duenio del vehiculo", on_delete=models.CASCADE,related_name="cliente")
    modelo = models.ForeignKey(Modelo, verbose_name="Modelo del auto", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return 'Auto con placas %s perteneciente a %s' % (self.placa, self.cliente)
