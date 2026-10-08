from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    # Exibe essas colunas na tabela do admin
    list_display = ('descricao', 'valor', 'cartao', 'data')
    
    # Adiciona um filtro lateral por cartão e por data
    list_filter = ('cartao', 'data')
    
    # Permite pesquisar pela descrição do produto
    search_fields = ('descricao',)
