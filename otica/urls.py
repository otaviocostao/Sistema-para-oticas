from . import views
from django.urls import path
from otica.views import ClienteListView, ClienteCreateView
from django.views.generic import RedirectView

app_name = 'otica'

urlpatterns = [
    path('', RedirectView.as_view(url='/login/'), name=''),
    path('login/', views.login, name='login'),
    path('inicio/', views.pag_inicial, name='pag_inicial'),
    path('clientes/', ClienteListView.as_view(), name='cliente'),
    path('receituario/', views.ver_receituario, name='ver_receituario'),
    path('cadastro_cliente/', ClienteCreateView.as_view(), name='cad_cliente'),
]

