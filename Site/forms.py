from django import forms

from Site.models import fale_conosco,cliente,aluguel




class fale_conoscoForm(forms.ModelForm):
    class Meta:
        model = fale_conosco
        fields = '__all__'



class aluguelForm(forms.ModelForm):
    class Meta:
        model = aluguel
        fields = '__all__'



class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

    