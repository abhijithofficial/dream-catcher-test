from rest_framework import generics, permissions
from .serializers import UserSerializer, UserListSerializer
from rest_framework.parsers import JSONParser
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import IntegrityError
from user.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class UserList(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # user = self.request.user
        return User.objects.all()


class UserSignUp(APIView):
    """
    Create User
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                success = True
                response = Response(
                    {'success': success, 'data': 'User Successfully Created.Please Signin'}, status=status.HTTP_201_CREATED)
                return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    """
    Verify User Login
    """

    def post(self, request, format='json'):
        data_error = {}
        data = request.data
        if 'username' not in data or 'password' not in data:
            success = False
            data = {'message': 'Username and Password is required'}
            response = Response(
                {'success': success, 'error': data}, status=status.HTTP_400_BAD_REQUEST)
            return response

        user = authenticate(
            request, username=data['username'], password=data['password'])
        if user is None:
            success = False
            data = {'message': 'Username or Password is incorrect'}
            response = Response(
                {'success': success, 'error': data}, status=status.HTTP_400_BAD_REQUEST)
            return response
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            data = {'token': str(token), 'redirect': '/userdata/'}
            success = True
            request.session['token'] = str(token)
            response = Response(
                {'success': success, 'data': data}, status=status.HTTP_200_OK)
            return response
