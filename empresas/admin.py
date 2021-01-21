from django.contrib import admin
from empresas.models import Empresas, Funcionario

class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_empresa', )
    list_display_links = ('id', 'nome_empresa', )

class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome_funcionario', 'get_name', )
    list_display_links = ('user', 'nome_funcionario', 'get_name', )    
    def get_name(self, obj):
        return obj.empresa
    get_name.admin_order_field  = 'id'  #Allows column order sorting
    get_name.short_description = 'Id empresa'  #Renames column head

admin.site.register(Empresas, EmpresasAdmin)
admin.site.register(Funcionario, FuncionariosAdmin)