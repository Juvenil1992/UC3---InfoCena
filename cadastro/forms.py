

from django import forms

from cadastro.models import Loja


class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = '__all__'