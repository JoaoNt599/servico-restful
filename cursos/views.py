from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvalicaoSerializer

# Create your views here.
class CursoAPIView(APIView):

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

class AvalicaoAPIView(APIView):

    def get(self, response):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvalicaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
