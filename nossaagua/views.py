from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Morador

def FaltaAgua(request):
    if request.method == 'GET':
        faltadeagua = {'id':1, 'resposta':'Sim'}
        return JsonResponse(faltadeagua)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            morador= Morador.objects.get(email=email)
        except Morador.DoesNotExist:
            morador=None

        if morador is not None:
            user = authenticate(username=morador.email, password=password)

            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'erro': 'Credenciais invalidas'}, status=400)
        else:
            return Response({'erro': 'Email não encontrado'}, status=400)