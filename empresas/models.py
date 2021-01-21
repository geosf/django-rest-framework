from django.db import models

# Create your models here.

class Empresas(models.Model):
    nome_empresa = models.CharField(max_length=255)
    class Meta:
        verbose_name = u'Empresa'
        verbose_name_plural = u'Empresas'
    
    def __str__(self):
        return self.nome_empresa

class Funcionario(models.Model):
    user = models.CharField(primary_key=True, max_length=25, editable=True)
    nome_funcionario = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresas, on_delete=models.RESTRICT, related_name='funcionarios')
    
    class Meta:
        verbose_name = u'Funcionario'
        verbose_name_plural = u'Funcionarios'
    
    def __str__(self):
        return self.nome_funcionario

