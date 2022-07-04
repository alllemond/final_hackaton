from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer, ChangepasswordSerializer, ForgotPasswordSerializer, ForgotPasswordCompleteSerializer


User = get_user_model()


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Thanks for registration! Please activate your account',
                status=201
                )
        return Response(serializer.errors, status=400)


class ActivationView(APIView):
    def get(self, request, activation_code):
        user = User.objects.filter(activation_code=activation_code).first()
        if user:
            user.is_active=True
            user.save()
            return Response(
                'Your account is active',
                status=200
            )
        return Response('Invalid activation code', status=400)

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response("Successfully signed out!")


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangepasswordSerializer(data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Password Changed Successfully')

class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_email()
            return Response("Mail send for recovering your password")


class ForgotPasswordCompleteView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Password changed successfully')

            