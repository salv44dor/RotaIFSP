from django.db import models

# Create your models here.
class Aviso(models.Model):
    class Destinatario(models.TextChoices):
        TODOS = 'TODOS', 'Todos'
        ALUNOS = 'ALUNOS', 'Alunos'
        MOTORISTAS = 'MOTORISTAS', 'Motoristas'

    id_aviso = models.AutoField(primary_key=True)
    titulo_aviso = models.CharField(max_length=100)
    descricao = models.TextField()
    autor = models.CharField(max_length=50)
    tipo_destinatario = models.CharField(
        max_length=10,
        choices=Destinatario.choices
    )

    class Meta:
        db_table = 'aviso'

    def __str__(self):
        return self.titulo_aviso