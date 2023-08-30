from pick import pick
import os
import time

fila = {
    'idosos': [],
    'gestantes': [],
    'deficiencia': [],
    'geral': []
}

ordem_chegada = 1

while True:
    os.system('cls')
    title = 'Selecione uma das opções abaixo'
    options = ['Retirar uma Senha', 'Verificar Situação da Fila', 'Sair']
    
    option, index = pick(options=options, title=title,
                         indicator='->', default_index=0)
    
    match index:
        case 0:
            if len(fila['idosos']) + len(fila['gestantes']) + len(fila['deficiencia']) + len(fila['geral']) != 10:
                title = 'Selecione a opção correspondente ao seu perfil'
                options = ['Idoso com mais de 65 anos', 'Gestantes ou Pessoas com Crianças de Colo',
                        'Portador de Deficiência', 'Público em Geral']

                option, index = pick(options=options, title=title,
                                    indicator='->', default_index=0)

                name = ''
                while name == '':
                    os.system('cls')
                    name = input('Digite seu nome completo: ')

                    if name.isspace() or name == '':
                        name = ''
                        print('Favor preencher com seu nome completo')
                        time.sleep(1.4)

                match index:
                    case 0:
                        fila['idosos'].append({'perfil': option, 'name': name, 'ordem_chegada': ordem_chegada})
                    case 1:
                        fila['gestantes'].append({'perfil': option, 'name': name, 'ordem_chegada': ordem_chegada})
                    case 2:
                        fila['deficiencia'].append({'perfil': option, 'name': name, 'ordem_chegada': ordem_chegada})
                    case 3:
                        fila['geral'].append({'perfil': option, 'name': name, 'ordem_chegada': ordem_chegada})

                ordem_chegada+=1
            
            else:
                title = 'Todas as 10 senhas foram retiradas. Favor voltar amanhã!'
                options = ['Início', 'Sair']

                option, index = pick(options=options, title=title,
                                    indicator='->', default_index=0)

                if index == 1:
                    exit()
        case 1:
            if (len(fila['deficiencia']) + len(fila['geral']) + len(fila['gestantes']) + len(fila['idosos'])) == 0:
                title = 'Não há ninguém na fila ou sendo atendido'

            elif (len(fila['deficiencia']) + len(fila['geral']) + len(fila['gestantes']) + len(fila['idosos'])) < 2:

                for x in fila:
                    for y in range(len(fila[x])):
                        title = f'{fila[x][y]["name"]} está sendo atendido nesse momento. Tendo como perfil "{fila[x][y]["perfil"]}"'

            else:

                index = 0
                for x in fila:
                    for y in range(len(fila[x])):
                        if index == 0:
                            title = f'{fila[x][y]["name"]} está sendo atendido nesse momento. Tendo como perfil "{fila[x][y]["perfil"]}"\nAbaixo é possível ver a fila atualmente\n\n'
                        else:
                            title += f"{index}º - Nome: {fila[x][y]['name']} - Perfil: {fila[x][y]['perfil']}\n"                            
                        
                        index+=1
                            

            options = ['Início', 'Sair']

            option, index = pick(options=options, title=title,
                                 indicator='->', default_index=0)

            if index == 1:
                exit()
        
        case 2:
            exit()