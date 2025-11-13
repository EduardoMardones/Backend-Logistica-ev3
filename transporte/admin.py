from django.contrib import admin

# Register your models here.
# transporte/admin.py
from django.contrib import admin
from .models import (
    Ruta, Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Carga, Despacho
)

# Configuración del Admin para Ruta
@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino', 'tipo_transporte', 'distancia_km')
    list_filter = ('tipo_transporte',)
    search_fields = ('origen', 'destino')
    ordering = ('origen',)

# Configuración del Admin para Vehiculo
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'tipo_vehiculo', 'capacidad_kg', 'activo')
    list_filter = ('tipo_vehiculo', 'activo')
    search_fields = ('patente', 'tipo_vehiculo')
    list_editable = ('activo',)

# Configuración del Admin para Aeronave
@admin.register(Aeronave)
class AeronaveAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'tipo_aeronave', 'capacidad_kg', 'activo')
    list_filter = ('tipo_aeronave', 'activo',)
    search_fields = ('matricula', 'tipo_aeronave')
    list_editable = ('activo',)

# Configuración del Admin para Conductor
@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'licencia', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'rut', 'licencia')
    list_editable = ('activo',)

# Configuración del Admin para Piloto
@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'certificacion', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'rut', 'certificacion')
    list_editable = ('activo',)

# Configuración del Admin para Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'telefono', 'correo_electronico')
    search_fields = ('nombre', 'rut', 'correo_electronico')
    list_filter = ('nombre',) # Añadido un filtro básico

# Configuración del Admin para Carga
@admin.register(Carga)
class CargaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'peso_kg', 'volumen_m3', 'cliente')
    list_filter = ('cliente',) # Filtro por cliente asociado
    search_fields = ('descripcion',)
    raw_id_fields = ('cliente',) # Permite buscar clientes por ID en lugar de un select grande

# Configuración del Admin para Despacho
@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'fecha_despacho', 'estado', 'ruta', 'get_transporte_info',
        'get_personal_info', 'carga', 'costo_envio'
    )
    list_filter = ('estado', 'fecha_despacho', 'ruta', 'vehiculo', 'aeronave', 'conductor', 'piloto')
    search_fields = (
        'estado', 'ruta__origen', 'ruta__destino', 'vehiculo__patente',
        'aeronave__matricula', 'conductor__nombre', 'piloto__nombre',
        'carga__descripcion'
    )
    date_hierarchy = 'fecha_despacho' # Permite navegar por fechas
    raw_id_fields = ('ruta', 'vehiculo', 'aeronave', 'conductor', 'piloto', 'carga') # Mejora la selección de ForeignKeys

    # Campos que se muestran para edición en el detalle del objeto
    fieldsets = (
        (None, {
            'fields': ('fecha_despacho', 'estado', 'costo_envio', 'carga')
        }),
        ('Detalles de la Ruta', {
            'fields': ('ruta',),
        }),
        ('Asignación de Transporte (Solo uno)', {
            'fields': ('vehiculo', 'aeronave'),
            'description': 'Elija un vehículo para transporte terrestre o una aeronave para transporte aéreo.'
        }),
        ('Asignación de Personal (Solo uno)', {
            'fields': ('conductor', 'piloto'),
            'description': 'Elija un conductor para transporte terrestre o un piloto para transporte aéreo.'
        }),
    )

    # Métodos para mostrar información combinada en list_display
    def get_transporte_info(self, obj):
        if obj.vehiculo:
            return f"Vehículo: {obj.vehiculo.patente}"
        elif obj.aeronave:
            return f"Aeronave: {obj.aeronave.matricula}"
        return "N/A"
    get_transporte_info.short_description = "Transporte Asignado"

    def get_personal_info(self, obj):
        if obj.conductor:
            return f"Conductor: {obj.conductor.nombre}"
        elif obj.piloto:
            return f"Piloto: {obj.piloto.nombre}"
        return "N/A"
    get_personal_info.short_description = "Personal Asignado"