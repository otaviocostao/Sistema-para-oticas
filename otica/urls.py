from . import views
from django.urls import path

app_name = 'otica'

urlpatterns = [
    path('', views.pag_inicial, name='pag_inicial')
]

