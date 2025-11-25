from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # URLs Função
    path('funcao/', views.funcao_list, name='funcao_list'),
    path('funcao/cadastrar/', views.funcao_create, name='funcao_create'),
    path('funcao/<int:pk>/editar/', views.funcao_update, name='funcao_update'),
    path('funcao/<int:pk>/excluir/', views.funcao_delete, name='funcao_delete'),

    # URLs Empresa
    path('empresa/', views.empresa_list, name='empresa_list'),
    path('empresa/cadastrar/', views.empresa_create, name='empresa_create'),
    path('empresa/<int:pk>/editar/', views.empresa_update, name='empresa_update'),
    path('empresa/<int:pk>/excluir/', views.empresa_delete, name='empresa_delete'),

    # URLs Vaga
    path('vaga/', views.vaga_list, name='vaga_list'),
    path('vaga/cadastrar/', views.vaga_create, name='vaga_create'),
    path('vaga/<int:pk>/editar/', views.vaga_update, name='vaga_update'),
    path('vaga/<int:pk>/excluir/', views.vaga_delete, name='vaga_delete'),
]
