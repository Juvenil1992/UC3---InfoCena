from django.shortcuts import render
from Site.forms import fale_conoscoForm

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
    Cliente = cliente.objects.order_by(Lower('nome'))
    return render(request,'cadastro.html', {'cliente': Cliente})

def Aluguel(request):
    Aluguel = aluguel.objects.order_by(Lower('nome'))
    return render(request,'aluguel.html',{'aluguel': Aluguel})

def Fale_conosco(request):
    form = fale_conoscoForm()
    return render(request,'fale_conosco.html', {'formulario': form})
