from django.views.generic import ListView, CreateView
from django.shortcuts import render
from core.models import Cliente

def login(request):
    
    return render(request, "otica/login.html")

def pag_inicial(request):

    return render(request, "otica/home.html")

class ClienteListView(ListView):
    template_name= "otica/cliente.html"
    model = Cliente
    context_object_name = "clientes"

class ClienteCreateView(CreateView):
    template_name= "otica/cadastra_cliente.html"
    model = Cliente
    fields = ["nome", "telefone", "endereco", "email", "cpf", "data_nasc"]


def ver_receituario(request):

    return render(request, "otica/buscar_receituario.html")