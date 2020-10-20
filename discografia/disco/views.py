from django.shortcuts import render, redirect
from .models import Musicas
from .forms import MusicaForm

def musica_list(request):
    template_name = 'musica_list.html'
    """
    Pegar somente a tabela "album" e tudo relacionado a ela, evitando abrir
    por completo o banco de dados.
    """
    musica_list = Musicas.objects.prefetch_related('album').all()
    
    musicas_titulo = []
    musicas_segundos = []
    for musicas in musica_list:
        musicas_titulo.append(musicas.titulo)
        musicas_segundos.append(musicas.segundos)
    context = {
        'musicas_segundos': musicas_segundos,
        'musicas_titulo': musicas_titulo,
        'musica_list': musica_list,
        }
    return render(request, template_name, context)

def musica_new(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disco:musicalist')
    else:
        form = MusicaForm()
        template_name = 'musica_new.html'
        context = {
            'form': form
            }
        return render(request, template_name, context)

def musica_delete(request, pk):
    musica_delete = Musicas.objects.get(pk=pk)
    musica_delete.delete()
    return redirect('disco:musicalist')

def musica_edit(request, pk):
    musica_edit = Musicas.objects.get(pk=pk)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica_edit)
        if form.is_valid():
            form.save()
            return redirect('disco:musicalist')
    else:
        form = MusicaForm(instance=musica_edit)
        template_name = 'musica_edit.html'
        context = {
            'form': form,
            'pk': pk,
            }
        return render(request, template_name, context)

def relatorio(request):
    template_name = 'relatório.html'
    musica_relatorio = Musicas.objects.prefetch_related('album').all()
    musicas_titulo = []
    musicas_segundos = []
    for musicas in musica_relatorio:
        musicas_titulo.append(musicas.titulo)
        musicas_segundos.append(musicas.segundos)
    context = {
        'musicas_segundos': musicas_segundos,
        'musicas_titulo': musicas_titulo,
        'musica_relatorio': musica_relatorio,
        }

    return render(request, template_name, context)