from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
            
    
class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user == user:
            serializer = UserDetailSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        
    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user == user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED) 
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
