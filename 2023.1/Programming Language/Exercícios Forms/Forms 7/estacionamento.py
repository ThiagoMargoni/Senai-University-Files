import os
import time

listVacancies, listReserved = [], []

for letters in ["A","B","C"]:
        for numbers in range(1,7):
            listVacancies.append(f'{letters}{numbers}')

while True:
    time.sleep(1)
    os.system('cls')
    printPark = ''

    for i in listVacancies:
        
        printPark+='\n' if i in ['B1', 'C1'] else ''

        if not i in listReserved:
            printPark += f'[ {i} ] '
        else:
            printPark += '[ --- ] '
    
    print(printPark)
    print('-------------------------------------------------')
    res = input('Insira a vaga que deseja usar: ')

    if res in listVacancies:
        if not res in listReserved:
            listReserved.append(res)
            print(f'Você estacionou na vaga {res}!')
        else:
            print('Vaga já em uso!')
        
        aux = input('Deseja estacionar em outra vaga? [S/N]: ')
        if aux == 'S':
            continue
        else:
            break
            
    else: 
        print('Insira um lugar existente')