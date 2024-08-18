from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('GET', 'POST'))
@csrf_exempt
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def livro_list_create(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data, template_name='assessments.html')
    
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, template_name='assessments.html')
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, template_name='assessments.html')

@api_view(('GET', 'POST'))
@csrf_exempt
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def livro_detail(request, pk):
    livro = Livro.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
