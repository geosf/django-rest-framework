from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from empresas.models import Empresas, Funcionario

# Create your tests here.

class TestEmpresas(TestCase):
  
  def setUp(self):
      self.empresa = mommy.make(Empresas, nome_empresa='Sony Music')
      
  def test_empresa_creation(self):
      self.assertTrue(isinstance(self.empresa, Empresas))
      self.assertEquals(self.empresa.__str__(), self.empresa.nome_empresa)

class TestFuncionario(TestCase):
  
  def setUp(self):
      self.funcionario = mommy.make(Funcionario, nome_funcionario='Geovani')
      
  def test_funcionario_creation(self):
      self.assertTrue(isinstance(self.funcionario, Funcionario))
      self.assertEquals(self.funcionario.__str__(), self.funcionario.nome_funcionario)