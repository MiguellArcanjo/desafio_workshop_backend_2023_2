from rest_framework import viewsets
from produtos.models import Produto, MarcaProduto, CategoriaProduto
from produtos.serializers import ProdutoSerializers, MarcaProdutoSerializers, CategoriaProdutoSerializer
from produtos.pagination import PaginacaoCustomizadaProdutos, PaginacaoCustomizadaCategorias, PaginacaoCustomizadaMarcas

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers
    pagination_class = PaginacaoCustomizadaProdutos

class MarcaProdutoViewSet(viewsets.ModelViewSet):
    queryset = MarcaProduto.objects.all()
    serializer_class = MarcaProdutoSerializers
    pagination_class = PaginacaoCustomizadaMarcas

class CategoriaProdutoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProduto.objects.all()
    serializer_class = CategoriaProdutoSerializer
    pagination_class = PaginacaoCustomizadaCategorias