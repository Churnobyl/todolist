from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class ArticleView(APIView):
    def post(self, request):
        pass
    
class ArticleDetailView(APIView):
    def get(self, request, pk):
        pass
    
    def patch(self, request, pk):
        pass
    
    def delete(self, request, pk):
        pass
