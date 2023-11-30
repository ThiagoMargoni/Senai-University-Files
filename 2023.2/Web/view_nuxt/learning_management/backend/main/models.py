# import os
# import django
# import datetime
# import pandas as pd
import re
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class Cargos(models.Model):
    nome = models.CharField(max_length=50)
    nivelAcesso = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Ambientes(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome


class Status(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome


class Usuarios(models.Model):
    nome = models.CharField(max_length=55)
    idUserFK = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    email = models.CharField(max_length=80)
    fone = models.CharField(max_length=15)
    ativo = models.BooleanField(default=False)
    idNivelAcessoFK = models.ForeignKey(Cargos, related_name="cargo", blank=True, null=True, on_delete=models.CASCADE)
    image = models.CharField(max_length=1500, blank=True, null=True)
    uid = models.CharField(max_length=55, blank=True, null=True)
    token = models.CharField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.nome


class Tarefas(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=1000)
    idSolicitanteFK = models.ForeignKey(Usuarios, on_delete=models.CASCADE)    
    idAmbienteFK = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    prazo = models.DateTimeField()
    dataInicio = models.DateTimeField(default=timezone.now())
    dataFim = models.DateTimeField(null=True, blank=True)
    idStatusFK = models.ForeignKey(Status, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class TarefasUsuarios(models.Model):
    idUsuarioFK = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    idTarefaFK = models.ForeignKey(Tarefas, on_delete=models.CASCADE)

    def __str__(self):
        return "ok"


class TarefasStatus(models.Model):    
    idStatusFK = models.ForeignKey(Status, on_delete=models.CASCADE)
    idTarefaFK = models.ForeignKey(Tarefas, on_delete=models.CASCADE)
    data = models.DateTimeField(null=True, blank=True, default=timezone.now())
    descricao = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return "ok"



class Fotos(models.Model):
    nome = models.CharField(max_length=55, blank=True, null=True)
    idTarefaFK = models.ForeignKey(Tarefas, on_delete=models.CASCADE, blank=True, null=True)
    idStatusFK = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=1500, blank=True, null=True)
    
    def __str__(self):
        return self.nome

