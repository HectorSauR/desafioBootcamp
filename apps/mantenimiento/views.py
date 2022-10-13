from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.user.models import User
from apps.auto.models import Auto
from apps.user.permissions import IsAdmin, IsClient
from .models import Mantenimiento
from .serializer import MantenimientoSerializer
# from .serializers import

# Create your views here.


class MantenimientoViewSet(viewsets.ModelViewSet):
    serializer_class = MantenimientoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete',
                           'set_password']:
            permission_classes = (IsAuthenticated, IsAdmin)
        elif self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated, IsAdmin | IsClient)
        else:
            permission_classes = (IsAuthenticated, )
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        # Aqui seria la manipulacion de la vista de los autos segun el cliente
        queryset = Mantenimiento.objects.all()
        user = self.request.user
        if user.type in [User.Type.CLIENTE]:
            autos_usuario = Auto.objects.filter(cliente=user.id)
            queryset = queryset.filter(auto = autos_usuario)

        return queryset