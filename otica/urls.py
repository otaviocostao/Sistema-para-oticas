from . import views
from django.urls import path

app_name = 'otica'

urlpatterns = [
    path('inicio', views.pag_inicial, name='pag_inicial'),
    path('cadastro', views.cadastro_cliente, name='cadastro_cliente'),
]

