from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Editora, Livro

def lista_livros(request):
    livros = Livro.objects.all()
#   livros = Livro.existentes.all()  # usando o gestor personalizado para obter apenas os livros existentes    
    return render(request, 'livros/lista.html', {'livros': livros})

def detalhes_livro(request, isbn):
    livro = get_object_or_404(Livro, isbn=isbn) # não está a utilizar filtros
    return render(request, 'livros/detalhes.html', {'livro': livro})
