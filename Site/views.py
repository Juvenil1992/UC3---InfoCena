from django.shortcuts import render
from Site.forms import fale_conoscoForm,clienteForm,aluguelForm

from cadastro.models import Produto,Loja
from Site.models import cliente,fale_conosco,aluguel
from django.db.models.functions import Lower

# Create your views here.

def index(request):
    return render(request, 'index.html')

def quem_somos(request):
    return render(request, 'quem_somos.html')

def produtos(request):
    produtos = Produto.objects.order_by(Lower('nome'))
    return render(request,'produtos.html',{'produtos' : produtos})

def lojas(request):
    lojas = Loja.objects.order_by(Lower('nome'))
    return render(request,'lojas.html',{'lojas' : lojas})

def cadastro(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    
    
    form = clienteForm()
    return render(request,'cadastro.html', {'formulario': form})


def Aluguel(request):
    if request.method == 'POST':
        form = aluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)

    form = aluguelForm()
    return render(request,'aluguel.html',{'formulario': form})


def Fale_conosco(request):
    if request.method == 'POST':
        form = fale_conoscoForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        
    form = fale_conoscoForm()
    return render(request,'fale_conosco.html', {'formulario': form})



