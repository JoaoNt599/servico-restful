from django.shortcuts import render
from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvalicaoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


# ========================= API V1 ==============================

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvalicaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(
                self.get_queryset(), 
                curso_id = self.kwargs.get('curso_pk'), 
                pk = self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk = self.kwargs.get('avaliacao_pk'))
    
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvalicoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()
    

# ========================= API V2 ==============================


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvalicaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.object.all()
    serializer_class = AvalicaoSerializer 
