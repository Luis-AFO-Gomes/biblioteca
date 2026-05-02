from django.db import models
from django.utils import timezone
# from django.db.models import Q

class LivroExistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Livro.Status.DISPONIVEL)
#   def get_queryset(self):    
#       disponiveis = Q(status=Livro.Status.DISPONIVEL)
#       emprestados = Q(status=Livro.Status.EMPRESTADO)
#       reservados = Q(status=Livro.Status.RESERVADO)
#       return super().get_queryset().filter(disponiveis | emprestados | reservados)

class Editora(models.Model):
    nipc = models.CharField(max_length=9, unique=True, primary_key=True)
    nome = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    morada = models.CharField(max_length=200)
    class Meta:
        ordering = ['nipc']
        indexes = [
            models.Index(fields=['nipc']),
            models.Index(fields=['nome']),
        ]

    def __str__(self):
        return self.nome

class Livro(models.Model):
    class Status(models.TextChoices):
        SUGERIDO = 'S', 'Sugerido'
        DISPONIVEL = 'D', 'Disponível'
        EMPRESTADO = 'E', 'Emprestado'
        RESERVADO = 'R', 'Reservado'
        RETIRADO = 'O', 'Retirado'
    isbn = models.CharField(max_length=13, unique=True, primary_key=True)
    titulo = models.CharField(max_length=200)
    idioma = models.CharField(max_length=3)
    tipo = models.CharField(max_length=50)
    tema = models.CharField(max_length=100)
    editora = models.ForeignKey(Editora, to_field='nipc', on_delete=models.PROTECT)
    data_pub = models.DateField()
    original = models.BooleanField(default=True)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.DISPONIVEL,
    )
    data_add = models.DateTimeField(default=timezone.now)
    objects = models.Manager()          # gestor de modelos padrão
    existentes = LivroExistManager()    # gestor de modelos personalizado para livros existentes
    class Meta:
        ordering = ['titulo']
        indexes = [
            models.Index(fields=['titulo']),
            models.Index(fields=['tipo']),
            models.Index(fields=['tema']),
        ]

    def __str__(self):
        return self.titulo
