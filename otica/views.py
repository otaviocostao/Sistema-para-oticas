from django.shortcuts import render

# Create your views here.
def pag_inicial(request):
    return render(request, "otica/home.html")