from django import forms

from Site.models import fale_conosco,cliente,aluguel




class fale_conoscoForm(forms.ModelForm):
    # nome = forms.CharField()
    # email = forms.EmailField()
    # telefone = forms.CharField()
    # assunto = forms.Textarea()
    class Meta:
        model = fale_conosco
        fields = '__all__'



class aluguelForm(forms.ModelForm):
    nome = forms.CharField()
    email = forms.EmailField()
    telefoneFixo = forms.CharField()
    telefoneCel = forms.CharField()
    class Meta:
        model = aluguel
        fields = '__all__'



class clienteForm(forms.ModelForm):
    nome = forms.CharField()
    cpf = forms.IntegerField()
    email = forms.EmailField()
    telefone = forms.CharField()
    class Meta:
        model = cliente
        fields = '__all__'

    