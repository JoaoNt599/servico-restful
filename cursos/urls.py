from django.urls import path
from .views import CursosAPIView, CursoAPIView, AvalicaoAPIView, AvalicoesAPIView, AvaliacaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvalicoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvalicaoAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/<int:avaliacao_pk>', AvalicaoAPIView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvalicoesAPIView.as_view(), name='avaliacoes'),
]
