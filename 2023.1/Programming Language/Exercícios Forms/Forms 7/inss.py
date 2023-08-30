from pick import pick
import os
import time

fila = {
    'idosos': [],
    'gestantes': [],
    'deficiencia': [],
    'geral': []
}

while True:
    os.system('cls')
    title = 'Selecione uma das opções abaixo'
    options = ['Retirar uma Senha', 'Verificar Situação da Fila',
               'Pesquisar seu Nome', 'Sair']

    option, index = pick(options=options, title=title,
                         indicator='->', default_index=0)

    match index:
        case 0:
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
                    fila['idosos'].append({'perfil': option, 'name': name})
                case 1:
                    fila['gestantes'].append({'perfil': option, 'name': name})
                case 2:
                    fila['deficiencia'].append(
                        {'perfil': option, 'name': name})
                case 3:
                    fila['geral'].append({'perfil': option, 'name': name})
        case 1:
            title = 'Selecione a opção da fila que deseja ver'
            options = ['Idoso com mais de 65 anos', 'Gestantes ou Pessoas com Crianças de Colo',
                       'Portador de Deficiência', 'Público em Geral']

            option, index = pick(options=options, title=title,
                                 indicator='->', default_index=0)

            if index == 0:
                index = 'idosos'
            elif index == 1:
                index = 'gestantes'
            elif index == 2:
                index = 'deficiencia'
            else:
                index = 'geral'

            if len(fila[index]) == 0:
                title = 'Não há ninguém nesta fila'
            elif len(fila[index]) < 2:
                print(fila[index][0])
                title = f'A pessoa que está sendo atendida na categoria de {fila[index][0]["perfil"]} é {fila[index][0]["name"]}'
            else:
                title = f'A pessoa que está sendo atendida na categoria de {fila[index][0]["perfil"]} é {fila[index][0]["name"]}\nAbaixo é possível ver a fila atualmente\n'

                for x in range(1, len(fila[index])):
                    title += f"{x} - {fila[index][x]['name']}\n"

            options = ['Início', 'Sair']

            option, index = pick(options=options, title=title,
                                 indicator='->', default_index=0)

            if index == 1:
                exit()

        case 2:
            name = ''
            while name == '':
                os.system('cls')
                name = input('Digite seu nome completo: ')

                if name.isspace() or name == '':
                    name = ''
                    print('Favor preencher com seu nome completo')
                    time.sleep(1.4)

            string = ''
            for x in fila:
                for y in fila[x]:
                    for z in fila[x][y]['name']:
                        if name in z:
                            if z == 0:
                                string = f'Você pode ser atendido'
                            else:
                                string = f'Você está na posição {z} da fila de {fila[x][y]["option"]}'
            if string != '':
                print(string)
            else:
                print('Seu nome não está cadastrado na fila')
                time.sleep(1.4)
        case 3:
            exit()
