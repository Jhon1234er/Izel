from rest_framework import serializers
from .models import Paciente
from .models import Usuario

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            'username', 'password', 'email', 'tipo_doc', 'num_doc', 'genero', 'rh',
            'telefono', 'fecha_nacimiento', 'tipo_poblacion', 'ocupacion', 'eps',
            'regimen', 'numero_seguro_social', 'first_name', 'last_name', 'imagen'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Paciente(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'tipo_doc', 'num_doc',
            'genero', 'rh', 'telefono', 'fecha_nacimiento', 'tipo_poblacion', 'ocupacion', 'eps'
        ]