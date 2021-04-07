from django.contrib.sessions.models import Session
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, authentication
from apps.users.serializers import UserDetailSerializer, UserSerializer
from datetime import datetime


class Register(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                if not created:
                    token.delete()
                    token = Token.objects.create(user=user)
                user_serializer = UserDetailSerializer(user)
                return Response({
                        'token': token.key,
                        'user': user_serializer.data
                    },
                    status=status.HTTP_200_OK
                )                
            else:
                return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'User or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def post(self, request):
        token = request.POST.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            user = token.user
            all_sessions = Session.objects.filter(expire_date_gte=datetime.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decode()
                    if user.id == int(session_data.get('_auth_user_id')):
                        session.delete()
            token.delete()
            return Response({'message': 'The session was closed.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Session not found.'}, status=status.HTTP_400_BAD_REQUEST)
