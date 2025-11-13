# logistica/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from transporte import views

# Router para la API REST (con prefijo 'api/')
router = DefaultRouter()
router.register(r'rutas', views.RutaViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'aeronaves', views.AeronaveViewSet)
router.register(r'conductores', views.ConductorViewSet)
router.register(r'pilotos', views.PilotoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'cargas', views.CargaViewSet)
router.register(r'despachos', views.DespachoViewSet)

# ==================== CONFIGURACIÓN DE SWAGGER/REDOC ====================
schema_view = get_schema_view(
    openapi.Info(
        title="Logística Global API",
        default_version='v1',
        description="""
        API REST para el sistema de gestión de Logística Global Ltda.
        
        ## Características:
        - Gestión de vehículos y aeronaves
        - Control de conductores y pilotos
        - Administración de rutas
        - Registro de despachos y cargas
        - Control de clientes
        
        ## Autenticación:
        Algunas rutas requieren autenticación JWT.
        """,
        terms_of_service="https://www.logisticaglobal.cl/terms/",
        contact=openapi.Contact(email="contacto@logisticaglobal.cl"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ==================== VISTAS HTML (Frontend) ====================
    # Home
    path('', views.home, name='home'),
    
    # Rutas para Ruta
    path('rutas/', views.RutaListView.as_view(), name='ruta-list'),
    path('rutas/crear/', views.RutaCreateView.as_view(), name='ruta-create'),
    path('rutas/<int:pk>/editar/', views.RutaUpdateView.as_view(), name='ruta-update'),
    path('rutas/<int:pk>/eliminar/', views.RutaDeleteView.as_view(), name='ruta-delete'),
    
    # Rutas para Vehiculo
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculo-list'),
    path('vehiculos/crear/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('vehiculos/<int:pk>/editar/', views.VehiculoUpdateView.as_view(), name='vehiculo-update'),
    path('vehiculos/<int:pk>/eliminar/', views.VehiculoDeleteView.as_view(), name='vehiculo-delete'),
    
    # Rutas para Aeronave
    path('aeronaves/', views.AeronaveListView.as_view(), name='aeronave-list'),
    path('aeronaves/crear/', views.AeronaveCreateView.as_view(), name='aeronave-create'),
    path('aeronaves/<int:pk>/editar/', views.AeronaveUpdateView.as_view(), name='aeronave-update'),
    path('aeronaves/<int:pk>/eliminar/', views.AeronaveDeleteView.as_view(), name='aeronave-delete'),
    
    # Rutas para Conductor
    path('conductores/', views.ConductorListView.as_view(), name='conductor-list'),
    path('conductores/crear/', views.ConductorCreateView.as_view(), name='conductor-create'),
    path('conductores/<int:pk>/editar/', views.ConductorUpdateView.as_view(), name='conductor-update'),
    path('conductores/<int:pk>/eliminar/', views.ConductorDeleteView.as_view(), name='conductor-delete'),
    
    # Rutas para Piloto
    path('pilotos/', views.PilotoListView.as_view(), name='piloto-list'),
    path('pilotos/crear/', views.PilotoCreateView.as_view(), name='piloto-create'),
    path('pilotos/<int:pk>/editar/', views.PilotoUpdateView.as_view(), name='piloto-update'),
    path('pilotos/<int:pk>/eliminar/', views.PilotoDeleteView.as_view(), name='piloto-delete'),
    
    # Rutas para Cliente
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente-delete'),
    
    # Rutas para Carga
    path('cargas/', views.CargaListView.as_view(), name='carga-list'),
    path('cargas/crear/', views.CargaCreateView.as_view(), name='carga-create'),
    path('cargas/<int:pk>/editar/', views.CargaUpdateView.as_view(), name='carga-update'),
    path('cargas/<int:pk>/eliminar/', views.CargaDeleteView.as_view(), name='carga-delete'),
    
    # Rutas para Despacho
    path('despachos/', views.DespachoListView.as_view(), name='despacho-list'),
    path('despachos/crear/', views.DespachoCreateView.as_view(), name='despacho-create'),
    path('despachos/<int:pk>/editar/', views.DespachoUpdateView.as_view(), name='despacho-update'),
    path('despachos/<int:pk>/eliminar/', views.DespachoDeleteView.as_view(), name='despacho-delete'),
    
    # ==================== API REST (con prefijo /api/) ====================
    path('api/', include((router.urls, 'transporte_api'), namespace='api')),
    
    # ==================== DOCUMENTACIÓN API ====================
    # Swagger UI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Autenticación DRF
    path('api-auth/', include('rest_framework.urls')),
]

# Servir archivos estáticos y media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)