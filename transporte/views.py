# transporte/views.py
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.views import FilterView

from .models import (
    Ruta, Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Carga, Despacho
)
from .serializers import (
    RutaSerializer, VehiculoSerializer, AeronaveSerializer, 
    ConductorSerializer, PilotoSerializer, ClienteSerializer, 
    CargaSerializer, DespachoSerializer
)
from .filters import (
    RutaFilter, VehiculoFilter, AeronaveFilter, ConductorFilter,
    PilotoFilter, ClienteFilter, CargaFilter, DespachoFilter
)

# ==================== VISTAS DE TEMPLATES ====================

# Vista Home
def home(request):
    context = {
        'total_vehiculos': Vehiculo.objects.filter(activo=True).count(),
        'total_aeronaves': Aeronave.objects.filter(activo=True).count(),
        'total_conductores': Conductor.objects.filter(activo=True).count(),
        'total_pilotos': Piloto.objects.filter(activo=True).count(),
        'total_despachos': Despacho.objects.count(),
        'despachos_pendientes': Despacho.objects.filter(estado='PENDIENTE').count(),
    }
    return render(request, 'home.html', context)

# ==================== CLASE BASE PARA LISTAS CON FILTROS Y ORDENAMIENTO ====================
class BaseFilteredListView(FilterView):
    """Vista base con filtros y ordenamiento"""
    paginate_by = 10
    
    def get_ordering(self):
        return self.request.GET.get('ordering', 'id')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.get_ordering()
        return queryset.order_by(ordering)

# ==================== VISTAS PARA RUTA ====================
class RutaListView(BaseFilteredListView):
    model = Ruta
    template_name = 'ruta/ruta_list.html'
    context_object_name = 'rutas'
    filterset_class = RutaFilter

class RutaCreateView(LoginRequiredMixin, CreateView):
    model = Ruta
    template_name = 'ruta/ruta_form.html'
    fields = ['origen', 'destino', 'tipo_transporte', 'distancia_km']
    success_url = reverse_lazy('ruta-list')

class RutaUpdateView(LoginRequiredMixin, UpdateView):
    model = Ruta
    template_name = 'ruta/ruta_form.html'
    fields = ['origen', 'destino', 'tipo_transporte', 'distancia_km']
    success_url = reverse_lazy('ruta-list')

class RutaDeleteView(LoginRequiredMixin, DeleteView):
    model = Ruta
    template_name = 'ruta/ruta_confirm_delete.html'
    success_url = reverse_lazy('ruta-list')

# ==================== VISTAS PARA VEHICULO ====================
class VehiculoListView(BaseFilteredListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'
    context_object_name = 'vehiculos'
    filterset_class = VehiculoFilter

class VehiculoCreateView(LoginRequiredMixin, CreateView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_form.html'
    fields = ['patente', 'tipo_vehiculo', 'capacidad_kg', 'activo']
    success_url = reverse_lazy('vehiculo-list')

class VehiculoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_form.html'
    fields = ['patente', 'tipo_vehiculo', 'capacidad_kg', 'activo']
    success_url = reverse_lazy('vehiculo-list')

class VehiculoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo-list')

# ==================== VISTAS PARA AERONAVE ====================
class AeronaveListView(BaseFilteredListView):
    model = Aeronave
    template_name = 'aeronave/aeronave_list.html'
    context_object_name = 'aeronaves'
    filterset_class = AeronaveFilter

class AeronaveCreateView(LoginRequiredMixin, CreateView):
    model = Aeronave
    template_name = 'aeronave/aeronave_form.html'
    fields = ['matricula', 'tipo_aeronave', 'capacidad_kg', 'activo']
    success_url = reverse_lazy('aeronave-list')

class AeronaveUpdateView(LoginRequiredMixin, UpdateView):
    model = Aeronave
    template_name = 'aeronave/aeronave_form.html'
    fields = ['matricula', 'tipo_aeronave', 'capacidad_kg', 'activo']
    success_url = reverse_lazy('aeronave-list')

class AeronaveDeleteView(LoginRequiredMixin, DeleteView):
    model = Aeronave
    template_name = 'aeronave/aeronave_confirm_delete.html'
    success_url = reverse_lazy('aeronave-list')

# ==================== VISTAS PARA CONDUCTOR ====================
class ConductorListView(LoginRequiredMixin, BaseFilteredListView):
    model = Conductor
    template_name = 'conductor/conductor_list.html'
    context_object_name = 'conductores'
    filterset_class = ConductorFilter

class ConductorCreateView(LoginRequiredMixin, CreateView):
    model = Conductor
    template_name = 'conductor/conductor_form.html'
    fields = ['nombre', 'rut', 'licencia', 'activo']
    success_url = reverse_lazy('conductor-list')

class ConductorUpdateView(LoginRequiredMixin, UpdateView):
    model = Conductor
    template_name = 'conductor/conductor_form.html'
    fields = ['nombre', 'rut', 'licencia', 'activo']
    success_url = reverse_lazy('conductor-list')

class ConductorDeleteView(LoginRequiredMixin, DeleteView):
    model = Conductor
    template_name = 'conductor/conductor_confirm_delete.html'
    success_url = reverse_lazy('conductor-list')

# ==================== VISTAS PARA PILOTO ====================
class PilotoListView(LoginRequiredMixin, BaseFilteredListView):
    model = Piloto
    template_name = 'piloto/piloto_list.html'
    context_object_name = 'pilotos'
    filterset_class = PilotoFilter

class PilotoCreateView(LoginRequiredMixin, CreateView):
    model = Piloto
    template_name = 'piloto/piloto_form.html'
    fields = ['nombre', 'rut', 'certificacion', 'activo']
    success_url = reverse_lazy('piloto-list')

class PilotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Piloto
    template_name = 'piloto/piloto_form.html'
    fields = ['nombre', 'rut', 'certificacion', 'activo']
    success_url = reverse_lazy('piloto-list')

class PilotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Piloto
    template_name = 'piloto/piloto_confirm_delete.html'
    success_url = reverse_lazy('piloto-list')

# ==================== VISTAS PARA CLIENTE ====================
class ClienteListView(BaseFilteredListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    context_object_name = 'clientes'
    filterset_class = ClienteFilter

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'cliente/cliente_form.html'
    fields = ['nombre', 'rut', 'direccion', 'telefono', 'correo_electronico']
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'cliente/cliente_form.html'
    fields = ['nombre', 'rut', 'direccion', 'telefono', 'correo_electronico']
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')

# ==================== VISTAS PARA CARGA ====================
class CargaListView(LoginRequiredMixin, BaseFilteredListView):
    model = Carga
    template_name = 'carga/carga_list.html'
    context_object_name = 'cargas'
    filterset_class = CargaFilter

class CargaCreateView(LoginRequiredMixin, CreateView):
    model = Carga
    template_name = 'carga/carga_form.html'
    fields = ['descripcion', 'peso_kg', 'volumen_m3', 'cliente']
    success_url = reverse_lazy('carga-list')

class CargaUpdateView(LoginRequiredMixin, UpdateView):
    model = Carga
    template_name = 'carga/carga_form.html'
    fields = ['descripcion', 'peso_kg', 'volumen_m3', 'cliente']
    success_url = reverse_lazy('carga-list')

class CargaDeleteView(LoginRequiredMixin, DeleteView):
    model = Carga
    template_name = 'carga/carga_confirm_delete.html'
    success_url = reverse_lazy('carga-list')

# ==================== VISTAS PARA DESPACHO ====================
class DespachoListView(LoginRequiredMixin, BaseFilteredListView):
    model = Despacho
    template_name = 'despacho/despacho_list.html'
    context_object_name = 'despachos'
    filterset_class = DespachoFilter

class DespachoCreateView(LoginRequiredMixin, CreateView):
    model = Despacho
    template_name = 'despacho/despacho_form.html'
    fields = ['fecha_despacho', 'estado', 'costo_envio', 'ruta', 
              'vehiculo', 'aeronave', 'conductor', 'piloto', 'carga']
    success_url = reverse_lazy('despacho-list')

class DespachoUpdateView(LoginRequiredMixin, UpdateView):
    model = Despacho
    template_name = 'despacho/despacho_form.html'
    fields = ['fecha_despacho', 'estado', 'costo_envio', 'ruta', 
              'vehiculo', 'aeronave', 'conductor', 'piloto', 'carga']
    success_url = reverse_lazy('despacho-list')

class DespachoDeleteView(LoginRequiredMixin, DeleteView):
    model = Despacho
    template_name = 'despacho/despacho_confirm_delete.html'
    success_url = reverse_lazy('despacho-list')

# ==================== VIEWSETS DE API REST ====================

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

class RutaViewSet(BaseViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    filterset_fields = ['tipo_transporte', 'origen', 'destino']
    search_fields = ['origen', 'destino']
    ordering_fields = ['id', 'origen', 'destino', 'distancia_km']
    permission_classes = [permissions.IsAuthenticated]

class VehiculoViewSet(BaseViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    filterset_fields = ['tipo_vehiculo', 'activo']
    search_fields = ['patente']
    ordering_fields = ['id', 'patente', 'capacidad_kg']

class AeronaveViewSet(BaseViewSet):
    queryset = Aeronave.objects.all()
    serializer_class = AeronaveSerializer
    filterset_fields = ['tipo_aeronave', 'activo']
    search_fields = ['matricula']
    ordering_fields = ['id', 'matricula', 'capacidad_kg']

class ConductorViewSet(BaseViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    filterset_fields = ['activo']
    search_fields = ['nombre', 'rut', 'licencia']
    ordering_fields = ['id', 'nombre']
    permission_classes = [permissions.IsAuthenticated]

class PilotoViewSet(BaseViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    filterset_fields = ['activo']
    search_fields = ['nombre', 'rut', 'certificacion']
    ordering_fields = ['id', 'nombre']
    permission_classes = [permissions.IsAuthenticated]

class ClienteViewSet(BaseViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filterset_fields = ['rut']
    search_fields = ['nombre', 'rut', 'correo_electronico']
    ordering_fields = ['id', 'nombre']

class CargaViewSet(BaseViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    filterset_fields = ['cliente', 'peso_kg']
    search_fields = ['descripcion']
    ordering_fields = ['id', 'peso_kg', 'volumen_m3']
    permission_classes = [permissions.IsAuthenticated]

class DespachoViewSet(BaseViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer
    filterset_fields = [
        'estado', 'ruta', 'conductor', 'piloto',
        'vehiculo', 'aeronave', 'carga', 'fecha_despacho'
    ]
    search_fields = ['estado']
    ordering_fields = ['id', 'fecha_despacho', 'costo_envio']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()