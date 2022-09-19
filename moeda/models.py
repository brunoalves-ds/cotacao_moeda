from django.db import models

# Create your models here.


class PegarInfo(models.Model):
    moedas = (
        ('BRL', 'Real'),
        ('EUR', 'Euro'),
        ('JPY', 'Iene')
    )
    data_inicio = models.DateField()
    data_fim = models.DateField()
    nome_moeda = models.CharField(max_length=25, choices=moedas)

    def __str__(self):
        return self.nome_moeda + " De " + str(self.data_inicio) + " Até " + str(self.data_fim)


