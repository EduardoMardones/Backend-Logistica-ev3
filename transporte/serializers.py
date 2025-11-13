# transporte/serializers.py
from rest_framework import serializers
from .models import (
    Ruta, Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Carga, Despacho
)

# Serializador para el modelo Ruta
class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__' # Incluye todos los campos del modelo

# Serializador para el modelo Vehiculo
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

# Serializador para el modelo Aeronave
class AeronaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeronave
        fields = '__all__'

# Serializador para el modelo Conductor
class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

# Serializador para el modelo Piloto
class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'

# Serializador para el modelo Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# Serializador para el modelo Carga
class CargaSerializer(serializers.ModelSerializer):
    # Opcional: Para mostrar el nombre del cliente en lugar de solo el ID
    # cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre') 
    class Meta:
        model = Carga
        fields = '__all__'
        # fields = ['id', 'descripcion', 'peso_kg', 'volumen_m3', 'cliente', 'cliente_nombre'] # Si usas el ReadOnlyField

# Serializador para el modelo Despacho
class DespachoSerializer(serializers.ModelSerializer):
    # Opcional: Para mostrar información detallada de los objetos relacionados
    # en lugar de solo sus IDs. Esto se conoce como 'nested serializers'.
    # ruta = RutaSerializer(read_only=True)
    # vehiculo = VehiculoSerializer(read_only=True)
    # aeronave = AeronaveSerializer(read_only=True)
    # conductor = ConductorSerializer(read_only=True)
    # piloto = PilotoSerializer(read_only=True)
    # carga = CargaSerializer(read_only=True)

    class Meta:
        model = Despacho
        fields = '__all__'

    # Si necesitas aplicar las validaciones del modelo Despacho (clean method)
    # también a nivel de serializer para la API, puedes sobrescribir el método validate
    # def validate(self, data):
    #     instance = Despacho(**data)
    #     try:
    #         instance.clean()
    #     except serializers.ValidationError as e:
    #         raise e # Re-lanzar la excepción de validación
    #     return data