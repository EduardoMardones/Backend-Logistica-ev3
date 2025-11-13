# transporte/models.py
from django.db import models

# CHOICES para campos específicos
TIPO_TRANSPORTE_CHOICES = [
    ('TERRESTRE', 'Terrestre'),
    ('AEREO', 'Aéreo'),
]

ESTADO_DESPACHO_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('EN_RUTA', 'En Ruta'),
    ('ENTREGADO', 'Entregado'),
    ('CANCELADO', 'Cancelado'), # Añadido un estado más por si acaso
]

# 1. Modelo RUTA
class Ruta(models.Model):
    origen = models.CharField(max_length=255, verbose_name="Origen")
    destino = models.CharField(max_length=255, verbose_name="Destino")
    tipo_transporte = models.CharField(
        max_length=50,
        choices=TIPO_TRANSPORTE_CHOICES,
        default='TERRESTRE',
        verbose_name="Tipo de Transporte"
    )
    distancia_km = models.FloatField(null=True, blank=True, verbose_name="Distancia (km)")

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"
        ordering = ['origen', 'destino']

    def __str__(self):
        return f"Ruta {self.id}: {self.origen} a {self.destino} ({self.tipo_transporte})"

# 2. Modelo VEHICULO
class Vehiculo(models.Model):
    patente = models.CharField(max_length=50, unique=True, verbose_name="Patente")
    tipo_vehiculo = models.CharField(max_length=50, verbose_name="Tipo de Vehículo") # Ej: Camión, Furgón, Bus
    capacidad_kg = models.IntegerField(verbose_name="Capacidad (kg)")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ['patente']

    def __str__(self):
        return f"{self.tipo_vehiculo} ({self.patente})"

# 3. Modelo AERONAVE
class Aeronave(models.Model):
    matricula = models.CharField(max_length=50, unique=True, verbose_name="Matrícula")
    tipo_aeronave = models.CharField(max_length=50, verbose_name="Tipo de Aeronave") # Ej: Avión de carga, Helicóptero
    capacidad_kg = models.IntegerField(verbose_name="Capacidad (kg)")
    activo = models.BooleanField(default=True, verbose_name="Activa")

    class Meta:
        verbose_name = "Aeronave"
        verbose_name_plural = "Aeronaves"
        ordering = ['matricula']

    def __str__(self):
        return f"{self.tipo_aeronave} ({self.matricula})"

# 4. Modelo CONDUCTOR
class Conductor(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre Completo")
    rut = models.CharField(max_length=15, unique=True, verbose_name="RUT")
    licencia = models.CharField(max_length=50, verbose_name="Número de Licencia")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

# 5. Modelo PILOTO
class Piloto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre Completo")
    rut = models.CharField(max_length=15, unique=True, verbose_name="RUT")
    certificacion = models.CharField(max_length=100, verbose_name="Certificación") # Ej: Tipo de aeronave, IFR
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Piloto"
        verbose_name_plural = "Pilotos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

# 6. Modelo CLIENTE
class Cliente(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre del Cliente")
    rut = models.CharField(max_length=15, unique=True, verbose_name="RUT")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    correo_electronico = models.EmailField(max_length=255, blank=True, null=True, verbose_name="Correo Electrónico")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# 7. Modelo CARGA
class Carga(models.Model):
    descripcion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Descripción de la Carga")
    peso_kg = models.FloatField(verbose_name="Peso (kg)")
    volumen_m3 = models.FloatField(blank=True, null=True, verbose_name="Volumen (m³)")
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name='cargas', verbose_name="Cliente")

    class Meta:
        verbose_name = "Carga"
        verbose_name_plural = "Cargas"
        ordering = ['descripcion', 'cliente']

    def __str__(self):
        return f"Carga {self.id}: {self.descripcion} ({self.peso_kg} kg)"

# 8. Modelo DESPACHO
class Despacho(models.Model):
    fecha_despacho = models.DateField(verbose_name="Fecha de Despacho")
    estado = models.CharField(
        max_length=50,
        choices=ESTADO_DESPACHO_CHOICES,
        default='PENDIENTE',
        verbose_name="Estado del Despacho"
    )
    costo_envio = models.FloatField(blank=True, null=True, verbose_name="Costo de Envío")

    # Relaciones - Nota: solo uno de vehiculo/aeronave y conductor/piloto debería estar presente
    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, related_name='despachos', verbose_name="Ruta")
    
    # Un despacho puede ser terrestre O aéreo, no ambos. Se configuran como opcionales.
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True, related_name='despachos_terrestres', verbose_name="Vehículo Asignado")
    aeronave = models.ForeignKey(Aeronave, on_delete=models.SET_NULL, null=True, blank=True, related_name='despachos_aereos', verbose_name="Aeronave Asignada")

    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, null=True, blank=True, related_name='despachos_conducidos', verbose_name="Conductor Asignado")
    piloto = models.ForeignKey(Piloto, on_delete=models.SET_NULL, null=True, blank=True, related_name='despachos_pilotados', verbose_name="Piloto Asignado")
    
    carga = models.ForeignKey(Carga, on_delete=models.PROTECT, related_name='despachos', verbose_name="Carga Asignada") # PROTECT para evitar borrar cargas si tienen despachos

    class Meta:
        verbose_name = "Despacho"
        verbose_name_plural = "Despachos"
        ordering = ['-fecha_despacho', 'estado'] # Ordenar por fecha de despacho descendente

    def __str__(self):
        transporte_asignado = self.vehiculo.patente if self.vehiculo else (self.aeronave.matricula if self.aeronave else "N/A")
        personal_asignado = self.conductor.nombre if self.conductor else (self.piloto.nombre if self.piloto else "N/A")
        return f"Despacho {self.id} - Ruta: {self.ruta.id} - Estado: {self.estado} - Transp: {transporte_asignado} - Personal: {personal_asignado}"

    # Validaciones personalizadas (opcional, pero buena práctica)
    def clean(self):
        # Asegurarse de que solo se asigna un tipo de transporte (vehículo o aeronave)
        if self.vehiculo and self.aeronave:
            raise models.ValidationError('Un despacho no puede tener asignado un vehículo y una aeronave al mismo tiempo.')
        if not self.vehiculo and not self.aeronave:
            raise models.ValidationError('Un despacho debe tener asignado un vehículo o una aeronave.')

        # Asegurarse de que solo se asigna un tipo de personal (conductor o piloto)
        if self.conductor and self.piloto:
            raise models.ValidationError('Un despacho no puede tener asignado un conductor y un piloto al mismo tiempo.')
        if not self.conductor and not self.piloto:
            raise models.ValidationError('Un despacho debe tener asignado un conductor o un piloto.')
        
        # Coherencia entre tipo de transporte y personal
        if self.vehiculo and self.piloto:
            raise models.ValidationError('Un despacho terrestre no puede tener un piloto.')
        if self.aeronave and self.conductor:
            raise models.ValidationError('Un despacho aéreo no puede tener un conductor.')


    def save(self, *args, **kwargs):
        self.full_clean() # Ejecutar la validación personalizada antes de guardar
        super().save(*args, **kwargs)