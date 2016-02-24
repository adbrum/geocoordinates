from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)

    class Meta:
        verbose_name_plural = 'pessoas'
        verbose_name = 'pessoa'

    def __str__(self):
        return self.nome


class Coordenada(models.Model):
    possoa = models.ForeignKey('Pessoa')
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.IntegerField('Número')
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('estado', max_length=10)
    longitude = models.FloatField('Longitude')
    latitude = models.FloatField('Latitude')

    class Meta:
        verbose_name_plural = 'coordenadas'
        verbose_name = 'coordenada'

    def __str__(self):
        return self.possoa.nome
