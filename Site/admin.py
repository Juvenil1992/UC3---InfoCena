from django.contrib import admin
from Site.models import MotivoContato,fale_conosco,aluguel,cliente

# Register your models here.

admin.site.register(MotivoContato)
admin.site.register(fale_conosco)
admin.site.register(aluguel)
admin.site.register(cliente)