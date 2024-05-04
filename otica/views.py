from django.shortcuts import render
from core.models import Cliente

def login(request):
    
    return render(request, "otica/login.html")

def pag_inicial(request):

    return render(request, "otica/home.html")

def cadastro_cliente(request):
    model = Cliente
    return render(request, "otica/cadastro_cliente.html")

def ver_receituario(request):

    return render(request, "otica/buscar_receituario.html")