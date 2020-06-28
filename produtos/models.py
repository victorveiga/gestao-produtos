from django.db import models

# Create your models here.
class Produto(models.Model):
    codigoBarras     = models.CharField(max_length=30)
    descricao        = models.CharField(max_length=50)
    precoCusto       = models.DecimalField(max_digits=9,decimal_places=2)
    precoVenda       = models.DecimalField(max_digits=9,decimal_places=2)
    unidadeMedida    = models.CharField(max_length=2)
    estoque          = models.DecimalField(max_digits=9,decimal_places=2)
    controlarEstoque = models.BooleanField()
    descontoMaximo   = models.DecimalField(max_digits=9,decimal_places=2)
    comissao         = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return 'Código: {}| Descrição: {}'.format(self.codigoBarras, self.descricao)