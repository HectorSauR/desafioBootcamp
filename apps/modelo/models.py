from django.db import models

# Create your models here.


class Marca (models.Model):

    name = models.CharField(max_length=50, verbose_name="Nombre")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.name


class Modelo (models.Model):

    name = models.CharField(max_length=50, verbose_name="Nombre")
    brand = models.ForeignKey(Marca, on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

    def __str__(self):
        return self.name
