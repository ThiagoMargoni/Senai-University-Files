import os
import time

listChairs, listReserved = [], []

for letters in ["A","B","C"]:
        for numbers in range(1,11):
            listChairs.append(f'{letters}{numbers}')

while True:
    time.sleep(1)
    os.system('cls')
    printChairs = ''

    for i in listChairs:
        
        printChairs+='\n' if i in ['B1', 'C1'] else ''

        if not i in listReserved:
            printChairs += f'[ {i} ] '
        else:
            printChairs += '[ --- ] '
    
    print(printChairs)
    print('----------------------------------------------------------------------')
    res = input('Insira a cadeira que deseja reservar: ')

    if res in listChairs:
        if not res in listReserved:
            listReserved.append(res)
            print(f'Cadeira {res} reservada!')
        else:
            print('Cadeira já reservada!')
        
        aux = input('Deseja reservar outro lugar? [S/N]: ')
        if aux == 'S':
            continue
        else:
            break
            
    else: 
        print('Insira um lugar existente')