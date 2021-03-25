
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.serializers import UserSerializer, UserDetailSerializer, UserListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
#from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated] # TokenHasReadWriteScope"""]
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserListSerializer(users, many=True)        
        return Response(users_serializer.data)


class UserDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticated]  # TokenHasReadWriteScope"""]

    def get(self, request, pk=None):
        if not pk is None:
            user = User.objects.filter(id=pk).first()
            if user: 
                user_serializer = UserDetailSerializer(user)
                return Response(user_serializer.data)
            else: 
                return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk is None:
            user = User.objects.filter(id=pk).first()
            if user: 
                user.delete()
                return Response({'message': 'User was removed successfully.'})
            else: 
                return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk is None:
            user = User.objects.filter(id=pk).first()
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    