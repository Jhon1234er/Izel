from django.urls import path
from .views import *


urlpatterns = [
    path('registro/', RegistroPacienteAPIView.as_view(), name='registro'),
    path('usuario/', UsuarioAutenticadoAPIView.as_view(), name='usuario'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
