from django.db import models

class Gasto(models.Model): 
    CARTAO_CHOICES = [
        ('adriana', 'Adriana'), 
        ('cassio', 'Cássio'),
       
    ]
    
    descricao = models.CharField(max_length=100, verbose_name="Descrição/Produto")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor R$")
    data = models.DateField(verbose_name="Data")  
    cartao = models.CharField(max_length=10, choices=CARTAO_CHOICES, verbose_name="Cartão")
    
    def __str__(self):
        return f"{self.descricao} - R$ {self.valor} ({self.get_cartao_display()})" 
    
