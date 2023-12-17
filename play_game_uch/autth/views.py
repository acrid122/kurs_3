from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from .forms import *
from sic.models import Stat
from sic.serializers import StatSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer, PasswordResetRequestSerializer, SetNewPasswordSerializer, LogoutUserSerializer
from .utils import send_code_user
from .models import OneTimePassword
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import logging



logger = logging.getLogger(__name__)


class RegisterApi(APIView):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'autth/reg.html', {'form': form})
    
    
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            send_code_user(user['email'])
            return Response({
                'status' : 201,
                'message' : 'Регистрация проведена успешно!',
                'data': serializer.data,
                'redirect': 'verify-email'
            })
        else:
            return Response({
                'status': 400,
                'errors': serializer.errors
            })



class VerifyUserEmail(APIView):
    def get(self, request):
        return render(request, 'autth/verify.html')
    

    def post(self, request):
        otpcode = request.data.get('otp')
        try:
            user_code_obj = OneTimePassword.objects.get(code=otpcode)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                'status' : 200,
                'message' : 'Верификация проведена успешно!',
                })
            return Response({
                'status' : 204,
                'message' : 'Код неверный! Юзер уже верифицирован!',
            })
        except OneTimePassword.DoesNotExist:
            return Response({'message': 'Passcode неверный', 'status': 400})



class LoginUserView(APIView):
    def get(self, request):
        return render(request, 'autth/login.html')

    def post(self, request):
        try:
            data = request.data
            print(data)
            logger.info(f"Received login request with data: {data}")

            serializer = LoginSerializer(data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)

            return Response({
                'data': serializer.data,
                'status': 200
            })
        except Exception as e:
            logger.error(f"Ошибка в процессе входа: {str(e)}")
            return Response({'error': 'Ошибка входа'}, status=400)


class TestAuthenticationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = {
            'message': 'Токены работают'
        }
        return Response({
            'data': data,
            'status': 200
        })
    


class PasswordResetRequestView(APIView):
    serializer_class=PasswordResetRequestSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response({
            'message':'Вам на почту была отправлена ссылка для смены пароля',
            'status': 200
            })
    

class PasswordResetConfirm(APIView):

    def get(self, request, uidb64, token):
        try:
            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({
                    'message':'Неверный токен или токен уже устарел',
                    'status' :401
                    })
            return Response({
                'success':True, 
                'message':'credentials is valid', 
                'uidb64':uidb64, 
                'token':token,
                'status': 200
                })

        except DjangoUnicodeDecodeError:
            return Response({
                'message':'Неверный токен или токен уже устарел',
                'status': 401
                })
        

class SetNewPasswordView(APIView):
    serializer_class=SetNewPasswordSerializer

    def patch(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'success':True, 
            'message':"Пароль успешно изменен",
            'status': 200
        })


class TestingAuthenticatedReq(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):

        data={
            'msg':'Все работает'
        }
        return Response({
            'data': data, 
            'status': 200
        })

class LogoutApiView(APIView):
    serializer_class=LogoutUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': 204
        })
# def index(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('sic')
#             except:
#                 form.add_error(None, 'Ошибка аутентификации')

#     else:
#         form = LoginForm()
#     return render(request, 'autth/index.html', {'form': form})
