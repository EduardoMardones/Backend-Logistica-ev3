# transporte/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crea un router y registra nuestros ViewSets con él.
router = DefaultRouter()
router.register(r'rutas', views.RutaViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'aeronaves', views.AeronaveViewSet)
router.register(r'conductores', views.ConductorViewSet)
router.register(r'pilotos', views.PilotoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'cargas', views.CargaViewSet)
router.register(r'despachos', views.DespachoViewSet)

# Las URLs de la API están ahora determinadas automáticamente por el router.
urlpatterns = [
    path('', include(router.urls)),
]