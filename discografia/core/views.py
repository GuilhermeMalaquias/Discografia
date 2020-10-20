from django.shortcuts import render
from disco.models import Musicas

def index(request):
    template_name = 'index.html'
    musica = Musicas.objects.prefetch_related('album').all()
    context = {
        'musica': musica
        }
    return render(request, template_name, context)
