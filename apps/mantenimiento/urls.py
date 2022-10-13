from rest_framework import routers

from .views import MantenimientoViewSet


router = routers.SimpleRouter()
router.register(r'mantenimiento', MantenimientoViewSet , 'mantenimiento')

urlpatterns = router.urls