from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=150, primary_key=True)

class Paciente(models.Model):
    nome = models.CharField(max_length=150, primary_key=True)
    # consulta = models.ForeignKey(Consulta, related_name='itens', on_delete=models.CASCADE)

class Consulta(models.Model):
    daa_hora = models.DateField(max_length=150, primary_key=True)
    paciente = models.ForeignKey(Paciente, related_name='itens', on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, related_name='itens', on_delete=models.CASCADE)



