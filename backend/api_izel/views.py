from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.contrib.auth import authenticate, login, get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class LoginAPIView(APIView):
    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Permitir login con email
        if '@' in username:
            User = get_user_model()
            try:
                user_obj = User.objects.get(email=username)
                username = user_obj.username
            except User.DoesNotExist:
                return Response({"error": "Usuario no encontrado"}, status=401)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # ✅ Guarda al usuario en la sesión
            return Response({
                "mensaje": "Inicio de sesión exitoso",
                "usuario": user.username,
                "tipo": user.__class__.__name__,
                "id": user.id
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)
        
class RegistroPacienteAPIView(APIView):
    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Paciente registrado con éxito"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioAutenticadoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "tipo": user.__class__.__name__,  # Por ejemplo: Paciente, Medico, Administrador
            "id": user.id
        })