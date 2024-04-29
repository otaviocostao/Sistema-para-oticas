from django.shortcuts import render
 

# Create your views here.
def pag_inicial(request):

    return render(request, "otica/home.html")

def cadastro_cliente(request):
    
    return render(request, "otica/cadastro_cliente.html")