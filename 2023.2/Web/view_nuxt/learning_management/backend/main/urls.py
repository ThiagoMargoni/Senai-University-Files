from django.urls import path
from .views import *

urlpatterns = [
    path("cargos/", CargosAPIView.as_view(), name='cargos'),
    path('cargos/<int:pk>/', CargosAPIView.as_view(), name='cargosParameters'),

    path("ambientes/", AmbientesAPIView.as_view(), name='ambientes'),
    path('ambientes/<int:pk>/', AmbientesAPIView.as_view(), name='ambientesParameters'),
   
    path("status/", StatusAPIView.as_view(), name='status'),
    path('status/<int:pk>/', StatusAPIView.as_view(), name='statusParameters'),
    
    path("tarefasStatus/", TarefasStatusAPIView.as_view(), name='tarefasStatus'),
    path('tarefasStatus/<int:pk>/', TarefasStatusAPIView.as_view(), name='tarefasStatusParameters'),

    path("usuarios/", UsuariosAPIView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>/', UsuariosAPIView.as_view(), name='usuariosParameters'),
    
    path("cadastroUsuario/", CadastroUsuariosAPIView.as_view(), name='cadastroUsuario'),

    path("tarefas/", TarefasAPIView.as_view(), name='tarefas'),
    path('tarefas/<int:pk>/', TarefasAPIView.as_view(), name='tarefasParameters'),
    
    path("tarefasUsuarios/", TarefasUsuariosAPIView.as_view(), name='tarefasUsuarios'),
    path('tarefasUsuarios/<int:pk>/', TarefasUsuariosAPIView.as_view(), name='tarefasUsuariosParameters'),

    path("fotos/", FotosAPIView.as_view(), name='fotos'),
    path('fotos/<int:pk>/', FotosAPIView.as_view(), name='fotosParameters'),
   
    path("requestActivate/<slug:uid>/<slug:token>/", RequestActivateUser.as_view(), name='requestActivate'),
    
    path("emailSender/<slug:type>/", EmailSenderAPIView.as_view(), name='emailSender'),
]
