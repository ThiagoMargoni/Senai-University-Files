from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

class detCargos(admin.ModelAdmin):
    list_display = ('id','nome', 'nivelAcesso')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detAmbientes(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detStatus(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detUsuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'fone', 'ativo', 'idNivelAcessoFK', 'idUserFK')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detTarefas(admin.ModelAdmin):
    list_display = ('id','nome', 'descricao', 'idSolicitanteFK', 'idAmbienteFK', 'prazo', 'dataInicio', 'dataFim', 'idStatusFK')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detTarefasUsuarios(admin.ModelAdmin):
    list_display = ('id','idUsuarioFK', 'idTarefaFK')
    list_display_links = ('id',)
    search_fields = ('idTarefaFK',)
    list_per_page = 10

class detTarefasStatus(admin.ModelAdmin):
    list_display = ('id','idStatusFK', 'idTarefaFK', 'data', 'descricao')
    list_display_links = ('id',)
    search_fields = ('idTarefaFK',)
    list_per_page = 10

class detFotos(admin.ModelAdmin):
    list_display = ('id','nome', 'idTarefaFK', 'idStatusFK', 'image')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10


class CustomUserAdmin(UserAdmin):
    list_display = (
        '__str__',
        'id',
        'email',
        'first_name',
        'last_name',
        # 'get_groups',
        'is_staff',
        'is_superuser',
    )
    # @admin.display(description='Grupos')
    # def get_groups(self, obj):
    #     groups = obj.groups.all()
    #     if groups:
    #         return ', '.join([group.name for group in groups])

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

 



admin.site.register(Cargos, detCargos)
admin.site.register(Ambientes, detAmbientes)
admin.site.register(Status, detStatus)
admin.site.register(Usuarios, detUsuarios)
admin.site.register(Tarefas, detTarefas)
admin.site.register(TarefasUsuarios, detTarefasUsuarios)
admin.site.register(TarefasStatus, detTarefasStatus)
admin.site.register(Fotos, detFotos)
