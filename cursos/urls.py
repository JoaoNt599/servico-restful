from django.urls import path
from .views import CursosAPIView, CursoAPIView, AvalicaoAPIView, AvalicoesAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/', AvalicoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:pk>', AvalicaoAPIView.as_view(), name='avaliacao')
]
