
from .models import *
from .serializers import *
import datetime
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.http import HttpResponseRedirect

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from djoser.utils import decode_uid
from django.contrib.auth.models import User
from django.core.mail import send_mail


from django.db.models import Count, Max


#niveis de acesso
can_deleteUser = 20
can_approveUser = 20

def managePermissions(username, activity):
    resp = {'approvement': False, 'usuario': None}
    user = User.objects.get(username='501')
    usuario = Usuarios.objects.get(idUserFK=user.id)
    resp['approvement'] = True
    resp['usuario'] = usuario

    # if username != None and activity != None:
    #   user = User.objects.get(username=username)
    #   usuario = Usuarios.objects.get(idUserFK=user.id)
    #   print("usuario encontrado:")
    #   print(usuario)

    #   if usuario.idNivelAcessoFK.nivelAcesso:
    #       resp['usuario'] = usuario

    #       if usuario.ativo == True:                    
    #         if (activity == 'getUsers' or 
    #             activity == 'postTask' or
    #             activity == 'getTasks' or
    #             activity == 'getTasksUsers' or
    #             activity == 'getPhotos' or
    #             activity == 'deleteTask' or
    #             activity == 'postStatus_Progresso' or
    #             activity == 'changeUsuario'):
    #             if usuario.idNivelAcessoFK.nivelAcesso > 1:
    #                 resp['approvement'] = True
    #         elif activity == 'postStatus_Encerrada':
    #             if usuario.idNivelAcessoFK.nivelAcesso > 3:
    #                 resp['approvement'] = True
    #         elif activity == 'getUsersToken':
    #             if usuario.idNivelAcessoFK.nivelAcesso > 15:
    #                 resp['approvement'] = True
        
    return resp

class EmailSenderAPIView(APIView):

#  permission_classes = (IsAuthenticated,)

 def get(self, request, type):
    sendTo = []
    sendTo.append('andre_savedra@hotmail.com')
    messageBody = "Mensagem de teste do andre"
    send_mail(
            'SGAE - Uma nova tarefa foi atribuída à você!',
            messageBody,
            'info@sgae501.com.br',
            sendTo,
            fail_silently=False,
    )
    return Response({"msg": "ok"})


 def post(self, request, type):
    
    messageResponse = ''
    if type != None and type != '':
        # NEW TASK
        if type == 'newTask' and request.data:

            payload = request.data

            sendTo = []
            tarefa = Tarefas.objects.get(id=payload[0]['idTarefaFK'])

            for task in payload:
                usuario = Usuarios.objects.get(id=task['idUsuarioFK'])
                if usuario.email != None and usuario.email != '':
                    sendTo.append(usuario.email)
                 

            # sendTo.append('apiza@sp.senai.br')

            messageBody = ('A tarefa de número #' 
            + str(tarefa.id) + ' - ' + str(tarefa.nome) + ', solicitada por '
            + str(tarefa.idSolicitanteFK.nome) + ','
            + ' foi atribuída à você! \n\n Vá até o sistema SGAE - Sistema de Gestão de Ambientes e Confira!'
            + '\n\n Acesse nosso sistema em: https://educacional.sgae501.com.br/')
          
            send_mail(
            'SGAE - Uma nova tarefa foi atribuída à você!',
            messageBody,
            'info@sgae501.com.br',
            sendTo,
            fail_silently=True,
            )

            messageResponse = 'sent'

        # NEW TASK STATUS
        if type == 'newTaskStatus' and request.data:

            payload = request.data
            print("payload")
            print(payload)

            sendTo = []
            tarefa = Tarefas.objects.get(id=payload[0]['idTarefaFK'])
            status = Status.objects.get(id=payload[0]['idStatusFK'])

            # requester email
            requester = tarefa.idSolicitanteFK.email

            if requester != None and requester != '':
                sendTo.append(tarefa.idSolicitanteFK.email)

            tarefaUsuarios = TarefasUsuarios.objects.filter(idTarefaFK=tarefa.id)
                        
            # employees email
            for taskUser in tarefaUsuarios:
                if taskUser.idUsuarioFK.email != None and taskUser.idUsuarioFK.email != '':
                    if sendTo.count(taskUser.idUsuarioFK.email) == 0:
                        sendTo.append(taskUser.idUsuarioFK.email)            

            # sendTo.append('apiza@sp.senai.br')

            print("Enviando para os emails:")
            print(sendTo)

            messageBody = ('A tarefa de número #' 
            + str(tarefa.id) + ' - ' + str(tarefa.nome) + ', solicitada por '
            + str(tarefa.idSolicitanteFK.nome) + ','
            + ' está em um novo Status: ' + str(status.nome) + '.\n\n Vá até o sistema SGAE - Sistema de Gestão de Ambientes e Localize-a!'
            + '\n\n Acesse nosso sistema em: https://educacional.sgae501.com.br/')
          
            send_mail(
            'SGAE - Novo Status da Tarefa #' + str(tarefa.id),
            messageBody,
            'info@sgae501.com.br',
            sendTo,
            fail_silently=True,
            )

            messageResponse = 'sent'

    return Response({"msg": messageResponse})


class RequestActivateUser(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, uid, token, format = None):
        userId = decode_uid(uid)
        print("RECEBIDO UID:")
        print(uid)
        print("decode uid:")
        print(userId)
        
        if userId:
            usuario = Usuarios.objects.get(idUserFK=userId)
            usuario.token = token
            usuario.uid = uid
            usuario.save()
            print("novo usuario:")
            print(usuario)
            return HttpResponseRedirect('https://educacional.sgae501.com.br/sucesso/')
        else:
            return HttpResponseRedirect('https://educacional.sgae501.com.br/erro/')
            

def getPagination(request, listItems):

    if 'page' in request.GET:
        try:
            parameter_page = request.GET['page']
            if (int(parameter_page) <= 0):
                parameter_page = '1'
            page = Paginator(listItems, 10)
            return [page.page(parameter_page), page.count, page.num_pages]
        except (EmptyPage, PageNotAnInteger):
            return [page.page(1), 0, 0]
    else:
        return [listItems, 0, 0]



class CargosAPIView(APIView):
    """
    API Cargos
    """
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, pk=''):       
        if 'nivel' in request.GET:            
            nivel = request.GET['nivel']
            cargos = Cargos.objects.filter(nivelAcesso=nivel)
            serializer = CargosSerializer(cargos, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            cargos = Cargos.objects.get(id=pk)
            serializer = CargosSerializer(cargos)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            cargos = Cargos.objects.all()
            serializer = CargosSerializer(cargos, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )


    def post(self, request):
        serializer = CargosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        cargos = Cargos.objects.get(id=pk)
        serializer = CargosSerializer(cargos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        cargos = Cargos.objects.get(id=pk)
        cargos.delete()
        return Response({"msg": "Apagado com sucesso"})



class AmbientesAPIView(APIView):
    """
    API Ambientes
    """
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            ambientes = Ambientes.objects.all()
            serializer = AmbientesSerializer(ambientes, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            ambientes = Ambientes.objects.get(id=pk)
            serializer = AmbientesSerializer(ambientes)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )


    def post(self, request):
        serializer = AmbientesSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        ambientes = Ambientes.objects.get(id=pk)
        serializer = AmbientesSerializer(ambientes, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        ambientes = Ambientes.objects.get(id=pk)
        ambientes.delete()
        return Response({"msg": "Apagado com sucesso"})


class StatusAPIView(APIView):
    """
    API Status
    """
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            status = Status.objects.all()
            serializer = StatusSerializer(status, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            status = Status.objects.get(id=pk)
            serializer = StatusSerializer(status)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )


    def post(self, request):
        serializer = StatusSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        status = Status.objects.get(id=pk)
        serializer = StatusSerializer(status, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        status = Status.objects.get(id=pk)
        status.delete()
        return Response({"msg": "Apagado com sucesso"})

class CadastroUsuariosAPIView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        message = 'Erro'

        print(request.data);

        if request.data['idUserFK']:

            user = User.objects.get(id=request.data['idUserFK'])
            if user:
                
                usuario = Usuarios.objects.filter(email=request.data['email'])
                if usuario:
                    # message = 'Erro: já existe'
                    message = 'Criado com sucesso'
                else:
                    serializer = UsuariosSerializerCadastro(data=request.data)      
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    message = 'Criado com sucesso'
            else:
                message = 'Erro: user não encontrado'

        return Response({"msg": message})
        #return Response({"id": serializer.data['id']})



class UsuariosAPIView(APIView):
    """
    API Usuarios
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        
        # GET USER WITH ACTIVATION STATUS
        if 'ativo' in request.GET:
            ativo = request.GET['ativo']

            permission = managePermissions(request.user, 'getUsers')

            if permission['approvement']:
                cargo = Cargos.objects.get(nivelAcesso=permission['usuario'].idNivelAcessoFK.nivelAcesso)
                otherUsers = Usuarios.objects.filter(ativo=ativo).filter(idNivelAcessoFK__nivelAcesso__lt=cargo.nivelAcesso)
                actualUser = Usuarios.objects.filter(id=permission['usuario'].id)                              
                # union users
                usuarios = actualUser | otherUsers
                serializer = UsuariosSerializer(usuarios, many=True)            
                return Response(
                    {
                        'data': serializer.data,
                        'total': 0,
                        'pages': 0
                    }
                )
            else:
                return Response({"msg": "no permission"})

            
        # GET USERS TO BE APPROVED (TOKEN EXISTS)  
        elif 'token' in request.GET:

            permission = managePermissions(request.user, 'getUsersToken')
            if permission['approvement']:
                usuarios = Usuarios.objects.exclude(uid__isnull=True)
                serializer = UsuariosSerializer(usuarios, many=True)            
                return Response(
                    {
                        'data': serializer.data,
                        'total': 0,
                        'pages': 0
                    }
                )
            else:
                return Response({"msg": "no permission"})
                    
        # GET USERS WITH TOKEN AND UID  
        elif 'uid' in request.GET:
            usuarios = Usuarios.objects.all()
            resp = getPagination(request, usuarios)
            serializer = UsuariosSerializerUidToken(resp[0], many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            ) 
        #GET ALL USERS
        elif pk == '':
            usuarios = Usuarios.objects.all()
            resp = getPagination(request, usuarios)
            serializer = UsuariosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        # GET USERS IN PRIMARY KEY
        else:
            usuarios = Usuarios.objects.get(idUserFK=pk)
            serializer = UsuariosSerializer(usuarios)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )


    def post(self, request):        
        serializer = UsuariosSerializerSimple(data=request.data, many=True)      
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):

        if 'change' in request.GET:
            permission = managePermissions(request.user, 'changeUsuario')

            if ((permission['approvement']) and (permission['usuario'].id == pk)):

                usuarios = Usuarios.objects.get(id=pk)
                serializer = UsuariosSerializerSimple(usuarios, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"msg": "Atualizado com sucesso"})                
            else:
                return Response({"msg": "no permission"})
        elif 'activation' in request.GET:
            # check user level
            message = ""
            if "id" in request.data:
                usuarioRequest = Usuarios.objects.get(id=request.data["id"])
                if usuarioRequest.idNivelAcessoFK.nivelAcesso >= can_deleteUser and usuarioRequest.ativo == True:
                    
                    if "status" in request.data:
                        # approve user
                        if request.data["status"] == True:
                            # get user to allow or deny
                            usuarios = Usuarios.objects.get(id=pk)
                            if usuarios.uid != '' and usuarios.token != '': 

                                djangoHost = request.get_host()
                                payload = {'uid': usuarios.uid, 'token': usuarios.token}
                                
                                url = "http://" + djangoHost +"/api/v1/users/activation/"
                                response = requests.post(url, data = payload)
                                print("url")
                                print(url)
                                print("payload")
                                print(payload)
                                print("response")
                                print(response)
                                print(response.text)

                                if response.status_code == 204:
                                    message = "approved"

                                    usuarios.ativo = True
                                    usuarios.uid = None
                                    usuarios.token = None
                                    usuarios.save()
                                else:       
                                    message = "error"
                            else:
                                message = "already approved"                                
                                
                        # reprove user
                        else:
                            usuarios = Usuarios.objects.get(id=pk)
                            usuarios.ativo = False
                            usuarios.uid = None
                            usuarios.token = None
                            usuarios.save()
                            
                            user = User.objects.filter(id=usuarios.idUserFK)
                            user.delete()
                            message = "disapproved"
                else:
                    message = "no permission"
            else:
                message = "request unrecognized"               
        
        print(message)            
        return Response({"msg": message})

    def delete(self, request, pk=''):        
              
        return Response({"msg": "Inativo"})


class TarefasAPIView(APIView):
    """
    API tarefas
    """
    # permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        
        if 'solicitante' in request.GET:  
            solicitante = request.GET['solicitante']
            tarefas = Tarefas.objects.filter(idSolicitanteFK=solicitante)
            resp = getPagination(request, tarefas)
            serializer = TarefasSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        elif 'ambiente' in request.GET:
            ambiente = request.GET['ambiente']
            tarefas = Tarefas.objects.filter(idAmbienteFK=ambiente)            
            resp = getPagination(request, tarefas)
            serializer = TarefasSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        elif 'ids' in request.GET:
            tarefas = Tarefas.objects.all()
            serializer = TarefasSerializerJustId(tarefas, many=True)
            return Response({
                'data': serializer.data,
                'total': 0,
                'pages': 0
            }) 
        elif pk != '':
            tarefas = Tarefas.objects.get(id=pk)            
            serializer = TarefasSerializer(tarefas)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )     
        elif 'all' in request.GET:
            tarefas = Tarefas.objects.all()
            resp = getPagination(request, tarefas)            
            serializer = TarefasSerializer(resp[0], many=True)
            return Response({
                'data': serializer.data,
                'total': resp[1],
                'pages': resp[2]
            })
        else:
            permission = managePermissions(request.user, 'getTasks')

            if permission['approvement']:
              #get actual job
              cargo = Cargos.objects.get(nivelAcesso=permission['usuario'].idNivelAcessoFK.nivelAcesso)
              #employees with small levels
              othersTarefasUsuarios = TarefasUsuarios.objects.filter(idUsuarioFK__idNivelAcessoFK__nivelAcesso__lt=cargo.nivelAcesso).only('idTarefaFK')
              #get actual person
              actualTarefasUsuarios = TarefasUsuarios.objects.filter(idUsuarioFK=permission['usuario'].id).only('idTarefaFK')
              #union queries
              tarefasUsuarios = othersTarefasUsuarios | actualTarefasUsuarios

            #   scripts to remove duplicates:
              unique_fields = ['idTarefaFK',]

              duplicates = (
                    tarefasUsuarios.values(*unique_fields)
                    .order_by()
                    .annotate(max_id=Max('id'), count_id=Count('id'))
                    .filter(count_id__gt=1)
              )

              excluders = None
              tarefasUsuariosFiltrada = None
              index = 0

              print("duplicates")
              print(duplicates)

              if(len(duplicates) > 0):
                  
                for duplicate in duplicates:
                    if index == 0:
                        excluders = tarefasUsuarios.filter(**{x: duplicate[x] for x in unique_fields}).exclude(id=duplicate['max_id'])
                    else:
                        excluders = (excluders | tarefasUsuarios.filter(**{x: duplicate[x] for x in unique_fields}).exclude(id=duplicate['max_id']))
                    index += 1                
                # .delete() add in query if i want exclude from database...'
                tarefasUsuariosFiltrada = tarefasUsuarios.exclude(id__in=excluders).order_by('id')
              else:
                print("DUPLICATE VAZIOOOO")
                tarefasUsuariosFiltrada = tarefasUsuarios
              
            
              resp = getPagination(request, tarefasUsuariosFiltrada)
              serializer = TarefasUsuariosSerializerIdTarefa(resp[0], many=True)
              return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
              )            
            else:
              return Response({"msg": "no permission"})
        

    def post(self, request):
        permission = managePermissions(request.user, 'postTask')

        if permission['approvement']:
            
            # usuario = Usuarios.objects.get(id=permission['usuario'].id)

            serializer = TarefasSerializerSimple(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()        
            # return Response({"msg": "Inserido com sucesso"})
            # return Response({"id": serializer.data['id']})
            return Response(serializer.data)
        

    def put(self, request, pk=''):
        tarefas = Tarefas.objects.get(id=pk)
        serializer = TarefasSerializerSimple(tarefas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        message = "no permission"
        permission = managePermissions(request.user, 'deleteTask')
        if permission['approvement']:
            tarefas = Tarefas.objects.get(id=pk)

        #   if tarefas.idSolicitanteFK.id == permission['usuario'].id:

            tarefas.delete()
            message = "Apagado com sucesso"
          
        return Response({"msg": message})


class TarefasUsuariosAPIView(APIView):
    """
    API tarefas
    """
    
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):

        # GET BY TASK ID (REDUCED)
        if 'tarefa' in request.GET:
                permission = managePermissions(request.user, 'getTasksUsers')

            # if permission['approvement']:              
                tarefa = request.GET['tarefa']
                tarefasUsuarios = TarefasUsuarios.objects.filter(idTarefaFK=tarefa)
                resp = getPagination(request, tarefasUsuarios)
                serializer = TarefasUsuariosSerializerReduced(resp[0], many=True)
                return Response(
                    {
                        'data': serializer.data,
                        'total': resp[1],
                        'pages': resp[2]
                    }
                )
            # else:
                # return Response({"msg": "no permission"})
                
        # GET ALL TASKS (COMPLETE)
        elif 'completa' in request.GET:            
            tarefasUsuarios = TarefasUsuarios.objects.all()
            resp = getPagination(request, tarefasUsuarios)
            serializer = TarefasUsuariosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        # GET TASKS, PHOTOS AND STATUS BY TASK ID  (COMPLETE)  
        elif 'tarefaCompletaStatusPhoto' in request.GET:
            tarefa = request.GET['tarefaCompletaStatusPhoto']
            tarefasUsuarios = TarefasUsuarios.objects.filter(idTarefaFK=tarefa)         
            resp = getPagination(request, tarefasUsuarios)
            serializer = TarefasUsuariosSerializer(resp[0], many=True)

            tarefasStatus = TarefasStatus.objects.filter(idTarefaFK=tarefa)
            resp = getPagination(request, tarefasStatus)
            serializerStatus = TarefasStatusSerializer(resp[0], many=True)

            fotos = Fotos.objects.filter(idTarefaFK=tarefa)
            resp = getPagination(request, fotos)
            serializerPhotos = FotosSerializer(resp[0], many=True)

            return Response(
                {
                    'data': serializer.data,
                    'status': serializerStatus.data,
                    'photos': serializerPhotos.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        # GET TASK BY ID (COMPLETE)
        elif 'tarefaCompleta' in request.GET:
            tarefa = request.GET['tarefaCompleta']
            tarefasUsuarios = TarefasUsuarios.objects.filter(idTarefaFK=tarefa)         
            resp = getPagination(request, tarefasUsuarios)
            serializer = TarefasUsuariosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,                    
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        # GET TASK BY USER ID (COMPLETE)
        elif 'usuario' in request.GET:            
            usuario = request.GET['usuario']
            tarefasUsuarios = TarefasUsuarios.objects.filter(idUsuarioFK=usuario)
            resp = getPagination(request, tarefasUsuarios)
            serializer = TarefasUsuariosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )        
        # GET TASK BY PK (COMPLETE)
        elif pk != '':            
            tarefasUsuarios = TarefasUsuarios.objects.get(id=pk)
            serializer = TarefasUsuariosSerializer(tarefasUsuarios)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        # GET ALL TASKS (COMPLETE)
        else:
            permission = managePermissions(request.user, 'getTasksUsers')

            if permission['approvement']:
            #   cargo = Cargos.objects.get(nivelAcesso=permission['usuario'].idNivelAcessoFK.nivelAcesso)
            #   othersTarefasUsuarios = TarefasUsuarios.objects.filter(idUsuarioFK__idNivelAcessoFK__nivelAcesso__lt=cargo.nivelAcesso)
            #   actualTarefasUsuarios = TarefasUsuarios.objects.filter(idUsuarioFK=permission['usuario'].id)
            #   tarefasUsuarios = othersTarefasUsuarios | actualTarefasUsuarios
              tarefasUsuarios = TarefasUsuarios.objects.all()
              resp = getPagination(request, tarefasUsuarios)
              serializer = TarefasUsuariosSerializer(resp[0], many=True)
              return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
              )
            else:
              return Response({"msg": "no permission"})


    def post(self, request):
        serializer = TarefasUsuariosSerializerSimple(data=request.data,  many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()       
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        tarefasUsuarios = TarefasUsuarios.objects.get(id=pk)
        serializer = TarefasUsuariosSerializerSimple(tarefasUsuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):

        message = "no permission"
        permission = managePermissions(request.user, 'deleteTask')
        if permission['approvement']:
            tarefasUsuarios = TarefasUsuarios.objects.get(id=pk)

        # if tarefasUsuarios.idTarefaFK.idSolicitanteFK.id == permission['usuario'].id:

            tarefasUsuarios.delete()
            message = "Apagado com sucesso"
          
        return Response({"msg": message})
        


class TarefasStatusAPIView(APIView):
    """
    API tarefasStatus
    """
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        
        if 'tarefa' in request.GET:
            tarefa = request.GET['tarefa']
            tarefasStatus = TarefasStatus.objects.filter(idTarefaFK=tarefa)
            resp = getPagination(request, tarefasStatus)
            serializer = TarefasStatusSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        elif 'status' in request.GET:
            status = request.GET['status']
            tarefasStatus = TarefasStatus.objects.filter(idStatusFK=status)
            resp = getPagination(request, tarefasStatus)
            serializer = TarefasStatusSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        elif pk == '':
            tarefasStatus = TarefasStatus.objects.all()
            serializer = TarefasStatusSerializer(tarefasStatus, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            tarefasStatus = TarefasStatus.objects.get(id=pk)
            resp = getPagination(request, tarefasStatus)
            serializer = TarefasStatusSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )


    def post(self, request):

        message = "no permission"

        status = Status.objects.get(id=request.data[0]['idStatusFK'])
        activity = ''
        if status.nome == 'Encerrada':
            activity = 'postStatus_Encerrada'
        else:
            activity = 'postStatus_Progresso'
        
        # permission = managePermissions(request.user, activity)
        # if permission['approvement']:
        tarefa = Tarefas.objects.get(id=request.data[0]['idTarefaFK'])
        if status.nome == 'Encerrada':
            # if tarefa.idSolicitanteFK.id == permission['usuario'].id:
                serializer = TarefasStatusSerializerSimple(data=request.data, many=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                message = 'Atualizado com sucesso'                
        else:
            serializer = TarefasStatusSerializerSimple(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            message = 'Atualizado com sucesso'        

        return Response({"msg": message})
                    
        

    def put(self, request, pk=''):
        tarefasStatus = TarefasStatus.objects.get(id=pk)
        serializer = TarefasStatusSerializer(tarefasStatus, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        tarefasStatus = TarefasStatus.objects.get(id=pk)
        tarefasStatus.delete()
        return Response({"msg": "Apagado com sucesso"})



class FotosAPIView(APIView):
    """
    API Fotos
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'tarefa' in request.GET:

            permission = managePermissions(request.user, 'getPhotos')

            if permission['approvement']:
                tarefa = request.GET['tarefa']
                fotos = Fotos.objects.filter(idTarefaFK=tarefa)
                resp = getPagination(request, fotos)
                serializer = FotosSerializer(resp[0], many=True)
                return Response(
                    {
                        'data': serializer.data,
                        'total': resp[1],
                        'pages': resp[2]
                    }
                )
            else:
                return Response({"msg": "no permission"})
        elif pk != '':
            fotos = Fotos.objects.get(id=pk)
            serializer = FotosSerializer(fotos)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            fotos = Fotos.objects.all()
            resp = getPagination(request, fotos)
            serializer = FotosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )


    def post(self, request):
        serializer = FotosSerializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        # return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        fotos = Fotos.objects.get(id=pk)
        serializer = FotosSerializer(fotos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        fotos = Fotos.objects.get(id=pk)
        fotos.delete()
        return Response({"msg": "Apagado com sucesso"})


