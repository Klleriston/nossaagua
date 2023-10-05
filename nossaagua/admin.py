from django.contrib import admin
from nossaagua.models import Morador, FaltouAgua

class Moradores(admin.ModelAdmin):
    list_display = ('id','nome', 'cpf', 'email', 'celular', 'rua', 'numero_casa', 'bairro', 'cep')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    
admin.site.register(Morador, Moradores)


class FaltaAgua(admin.ModelAdmin):
    list_display =['respostafalta']
    list_display_links = ['respostafalta']
    search_fields = ['resposta',]
    
admin.site.register(FaltouAgua, FaltaAgua)


