from django.db import models

class Bandas(models.Model):
    nome = models.CharField('Bandas', max_length=200)

    class Meta:
        verbose_name = 'Banda'
        verbose_name_plural = 'Bandas'
        ordering = ['-nome']
    def __str__(self):
        return self.nome

class Albuns(models.Model):
    titulo = models.CharField('Titulo', max_length=200)
    banda = models.ForeignKey(Bandas, on_delete=models.PROTECT, verbose_name='Banda')
    data = models.DateTimeField('Criado em', auto_now_add=True)
    #Nao esta no escopo do trabalho, mas irei adicionar para manter um "Controle"...
    data_update = models. DateTimeField('Modificado', auto_now=True)

    class Meta:
        verbose_name = 'Álbum'
        verbose_name_plural = 'Álbuns'
    def __str__(self):
        return self.titulo
        
class Musicas(models.Model):
    titulo = models.CharField('Musica', max_length=200)
    segundos = models.IntegerField('Segundos')
    album = models.ForeignKey(Albuns, on_delete=models.PROTECT, verbose_name='Álbum')
    class Meta:
        verbose_name = 'Musica'
        verbose_name_plural = 'Musicas'
        ordering = ['-titulo']
    def __str__(self):
        return self.titulo