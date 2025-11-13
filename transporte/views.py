from django.shortcuts import render

# Create your views here.
# transporte/views.py
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Ruta, Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Carga, Despacho
)
from .serializers import (
    RutaSerializer, VehiculoSerializer, AeronaveSerializer, ConductorSerializer, PilotoSerializer,
    ClienteSerializer, CargaSerializer, DespachoSerializer
)

# Base para ViewSets que no requieren autenticación estricta (o se define a nivel de método)
class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny] # Por defecto, permitimos cualquier acceso. Se puede sobrescribir.
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] # Filtros comunes

# 1. ViewSet para Rutas
class RutaViewSet(BaseViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    filterset_fields = ['tipo_transporte', 'origen', 'destino'] # Añadido origen y destino como filtros
    search_fields = ['origen', 'destino']
    # Acceso a informes de rutas -> Requiere autenticación
    permission_classes = [permissions.IsAuthenticated]

# 2. ViewSet para Vehículos
class VehiculoViewSet(BaseViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    filterset_fields = ['tipo_vehiculo', 'activo'] # Filtro por tipo de vehículo y estado activo
    search_fields = ['patente']

# 3. ViewSet para Aeronaves
class AeronaveViewSet(BaseViewSet):
    queryset = Aeronave.objects.all()
    serializer_class = AeronaveSerializer
    filterset_fields = ['tipo_aeronave', 'activo'] # Filtro por tipo de aeronave y estado activo
    search_fields = ['matricula']

# 4. ViewSet para Conductores
class ConductorViewSet(BaseViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    filterset_fields = ['activo'] # Filtro por estado activo del conductor
    search_fields = ['nombre', 'rut', 'licencia']
    # Gestión de conductores -> Solo personal autorizado (autenticado)
    permission_classes = [permissions.IsAuthenticated]

# 5. ViewSet para Pilotos
class PilotoViewSet(BaseViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    filterset_fields = ['activo'] # Filtro por estado activo del piloto
    search_fields = ['nombre', 'rut', 'certificacion']
    # Gestión de pilotos -> Solo personal autorizado (autenticado)
    permission_classes = [permissions.IsAuthenticated]

# 6. ViewSet para Clientes
class ClienteViewSet(BaseViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filterset_fields = ['rut'] # Filtro por RUT del cliente
    search_fields = ['nombre', 'rut', 'correo_electronico']

# 7. ViewSet para Cargas
class CargaViewSet(BaseViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    filterset_fields = ['cliente', 'peso_kg'] # Filtro por cliente y peso
    search_fields = ['descripcion']
    # Acceso a informes de carga -> Requiere autenticación
    permission_classes = [permissions.IsAuthenticated]

# 8. ViewSet para Despachos
class DespachoViewSet(BaseViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer
    # Filtros avanzados: estado, ruta, conductor/piloto, vehículo/aeronave, carga, fecha
    filterset_fields = [
        'estado', 'ruta', 'conductor', 'piloto',
        'vehiculo', 'aeronave', 'carga', 'fecha_despacho'
    ]
    search_fields = ['estado'] # Permite buscar por texto en el estado
    # Registro de nuevos despachos -> Solo usuarios autenticados
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()