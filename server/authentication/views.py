from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import generics, status


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']


    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
    status=status.HTTP_200_OK)
# Si no es correcto devolvemos un error en la petición
        return Response( status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer