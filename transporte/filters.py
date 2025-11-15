# transporte/filters.py
import django_filters
from django import forms
from .models import (
    Ruta, Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Carga, Despacho
)


class RutaFilter(django_filters.FilterSet):
    """Filtros para Rutas"""
    origen = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Origen',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por origen...'})
    )
    destino = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Destino',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por destino...'})
    )
    tipo_transporte = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Tipo de Transporte',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TERRESTRE o AEREO'})
    )
    distancia_min = django_filters.NumberFilter(
        field_name='distancia_km',
        lookup_expr='gte',
        label='Distancia mínima (km)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 100'})
    )
    distancia_max = django_filters.NumberFilter(
        field_name='distancia_km',
        lookup_expr='lte',
        label='Distancia máxima (km)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 500'})
    )

    class Meta:
        model = Ruta
        fields = ['origen', 'destino', 'tipo_transporte']


class VehiculoFilter(django_filters.FilterSet):
    """Filtros para Vehículos"""
    patente = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Patente',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por patente...'})
    )
    tipo_vehiculo = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Tipo de Vehículo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Camión, Furgón, etc.'})
    )
    # CAMBIO IMPORTANTE: Usar ChoiceFilter en lugar de BooleanFilter
    activo = django_filters.ChoiceFilter(
        label='Estado',
        choices=[('', 'Todos'), ('true', 'Solo activos'), ('false', 'Solo inactivos')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=None
    )
    capacidad_min = django_filters.NumberFilter(
        field_name='capacidad_kg',
        lookup_expr='gte',
        label='Capacidad mínima (kg)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1000'})
    )
    capacidad_max = django_filters.NumberFilter(
        field_name='capacidad_kg',
        lookup_expr='lte',
        label='Capacidad máxima (kg)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10000'})
    )

    class Meta:
        model = Vehiculo
        fields = ['patente', 'tipo_vehiculo', 'activo']


class AeronaveFilter(django_filters.FilterSet):
    """Filtros para Aeronaves"""
    matricula = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Matrícula',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por matrícula...'})
    )
    tipo_aeronave = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Tipo de Aeronave',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Avión, Helicóptero, etc.'})
    )
    # CAMBIO IMPORTANTE: Usar ChoiceFilter en lugar de BooleanFilter
    activo = django_filters.ChoiceFilter(
        label='Estado',
        choices=[('', 'Todos'), ('true', 'Solo activas'), ('false', 'Solo inactivas')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=None
    )
    capacidad_min = django_filters.NumberFilter(
        field_name='capacidad_kg',
        lookup_expr='gte',
        label='Capacidad mínima (kg)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 5000'})
    )

    class Meta:
        model = Aeronave
        fields = ['matricula', 'tipo_aeronave', 'activo']


class ConductorFilter(django_filters.FilterSet):
    """Filtros para Conductores"""
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre...'})
    )
    rut = django_filters.CharFilter(
        lookup_expr='icontains',
        label='RUT',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'})
    )
    licencia = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Licencia',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de licencia...'})
    )
    # CAMBIO IMPORTANTE: Usar ChoiceFilter en lugar de BooleanFilter
    activo = django_filters.ChoiceFilter(
        label='Estado',
        choices=[('', 'Todos'), ('true', 'Solo activos'), ('false', 'Solo inactivos')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=None
    )

    class Meta:
        model = Conductor
        fields = ['nombre', 'rut', 'licencia', 'activo']


class PilotoFilter(django_filters.FilterSet):
    """Filtros para Pilotos"""
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre...'})
    )
    rut = django_filters.CharFilter(
        lookup_expr='icontains',
        label='RUT',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'})
    )
    certificacion = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Certificación',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de certificación...'})
    )
    # CAMBIO IMPORTANTE: Usar ChoiceFilter en lugar de BooleanFilter
    activo = django_filters.ChoiceFilter(
        label='Estado',
        choices=[('', 'Todos'), ('true', 'Solo activos'), ('false', 'Solo inactivos')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=None
    )

    class Meta:
        model = Piloto
        fields = ['nombre', 'rut', 'certificacion', 'activo']


class ClienteFilter(django_filters.FilterSet):
    """Filtros para Clientes"""
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre...'})
    )
    rut = django_filters.CharFilter(
        lookup_expr='icontains',
        label='RUT',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'})
    )
    correo_electronico = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'})
    )
    telefono = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Teléfono',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'})
    )

    class Meta:
        model = Cliente
        fields = ['nombre', 'rut', 'correo_electronico', 'telefono']


class CargaFilter(django_filters.FilterSet):
    """Filtros para Cargas"""
    descripcion = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Descripción',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar en descripción...'})
    )
    cliente = django_filters.ModelChoiceFilter(
        queryset=Cliente.objects.all(),
        label='Cliente',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    peso_min = django_filters.NumberFilter(
        field_name='peso_kg',
        lookup_expr='gte',
        label='Peso mínimo (kg)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 100'})
    )
    peso_max = django_filters.NumberFilter(
        field_name='peso_kg',
        lookup_expr='lte',
        label='Peso máximo (kg)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 5000'})
    )
    volumen_min = django_filters.NumberFilter(
        field_name='volumen_m3',
        lookup_expr='gte',
        label='Volumen mínimo (m³)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1'})
    )

    class Meta:
        model = Carga
        fields = ['descripcion', 'cliente']


class DespachoFilter(django_filters.FilterSet):
    """Filtros para Despachos"""
    estado = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Estado',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PENDIENTE, EN RUTA, ENTREGADO'})
    )
    fecha_desde = django_filters.DateFilter(
        field_name='fecha_despacho',
        lookup_expr='gte',
        label='Fecha desde',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    fecha_hasta = django_filters.DateFilter(
        field_name='fecha_despacho',
        lookup_expr='lte',
        label='Fecha hasta',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    ruta = django_filters.ModelChoiceFilter(
        queryset=Ruta.objects.all(),
        label='Ruta',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    vehiculo = django_filters.ModelChoiceFilter(
        queryset=Vehiculo.objects.all(),
        label='Vehículo',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    aeronave = django_filters.ModelChoiceFilter(
        queryset=Aeronave.objects.all(),
        label='Aeronave',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    conductor = django_filters.ModelChoiceFilter(
        queryset=Conductor.objects.all(),
        label='Conductor',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    piloto = django_filters.ModelChoiceFilter(
        queryset=Piloto.objects.all(),
        label='Piloto',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    costo_min = django_filters.NumberFilter(
        field_name='costo_envio',
        lookup_expr='gte',
        label='Costo mínimo',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10000'})
    )
    costo_max = django_filters.NumberFilter(
        field_name='costo_envio',
        lookup_expr='lte',
        label='Costo máximo',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 500000'})
    )

    class Meta:
        model = Despacho
        fields = ['estado', 'ruta', 'vehiculo', 'aeronave', 'conductor', 'piloto']