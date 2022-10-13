from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Mantenimiento


@receiver(pre_save, sender=Mantenimiento)
def mantenimiento_post_save(sender, instance, created, **kwargs):
    print('Mantenimiento guardado')

    kilometrajeAuto = instance.Mantenimiento.auto.kilometraje

    instance.Mantenimiento.kilometraje = kilometrajeAuto
    instance.save()
