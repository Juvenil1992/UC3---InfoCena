

from django import forms

from cadastro.models import Loja,Produto


class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = '__all__'


class ProdutosForm(forms.ModelForm):
    nome = forms.CharField(label="Nome do Produto:")
    preco = forms.DecimalField(label="Preço:")
    destaque = forms.BooleanField(label="Destacar Produto?")
    class Meta:

        model = Produto
        fields = '__all__'