from rest_framework import viewsets
from empresas.api import serializers
from empresas import models

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = models.Empresas.objects.all()
    serializer_class = serializers.EmpresasSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = models.Funcionario.objects.all()
    serializer_class = serializers.FuncionarioSerializer
