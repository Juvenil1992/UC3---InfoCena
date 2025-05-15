from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def quem_somos(request):
    return render(request, 'quem_somos.html')
