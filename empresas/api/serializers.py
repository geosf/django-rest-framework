from rest_framework import serializers
from empresas import models

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Funcionario
        fields = ('user', 'nome_funcionario')

class EmpresasSerializer(serializers.ModelSerializer):
    funcionarios = FuncionarioSerializer(many=True, read_only=True)
    class Meta:
        model = models.Empresas
        fields = ('id', 'nome_empresa', 'funcionarios')
