from django.shortcuts import render
from rest_framework.views import APIView


class UserView(APIView):
    def post(self, request):
        pass
    
class UserDetailView(APIView):
    def get(self, request, pk):
        pass
    
    def patch(self, request, pk):
        pass
    
    def delete(self, request, pk):
        pass
