from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm
from .models import Produto

# Create your views here.
@login_required
def index(request):
    produtos = Produto.objects.all()
    return render(request, 'list_produtos.html', {'produtos': produtos})

@login_required
def create(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('produtos')

    return render(request, 'cad_produtos.html', {'form': form}) 

@login_required
def update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produtos')

    return render(request, 'cad_produtos.html', {'form': form})

@login_required
def delete(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        produto.delete()

    return redirect('produtos')
