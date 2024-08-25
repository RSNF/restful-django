from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from core.models import Livro
from ..serializers import LivroSerializer

class LivroView(APIView):

    def get(self, request, id=None, format=None):

        if id is not None:
            livro = Livro.objects.get(id=id)
            serializer = LivroSerializer(livro, many=False)
        else:  
            livros = Livro.objects.all()
            serializer = LivroSerializer(livros, many=True)

        return Response(serializer.data)
    
    def post(self, request, format=None):

        serializer = LivroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):

        livro = Livro.objects.get(id=id)

        serializer = LivroSerializer(livro, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        livro = Livro.objects.get(id=id)
        livro.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

