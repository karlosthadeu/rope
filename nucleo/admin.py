from django.contrib import admin
from .models import Materia, PlanoDeEstudo, Publicacao, Historico, Chamado

# Registre seus models aqui
admin.site.register(Materia)
admin.site.register(Publicacao)
admin.site.register(PlanoDeEstudo)
admin.site.register(Historico)
admin.site.register(Chamado)