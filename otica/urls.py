from . import views
from django.urls import path

app_name = 'otica'

urlpatterns = [
    path('', views.login, name='login'),
    path('inicio', views.pag_inicial, name='pag_inicial'),
    path('clientes', views.cadastro_cliente, name='cadastro_cliente'),
    path('receituario', views.ver_receituario, name='ver_receituario'),
]
    
