from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = [
            'codigoBarras'    ,
            'descricao'       ,
            'precoCusto'      ,
            'precoVenda'      ,
            'unidadeMedida'   ,
            'estoque'         ,
            'controlarEstoque',
            'descontoMaximo'  ,
            'comissao'        
        ]