# while True:
#     tentativas = 0
#     n1,n2,n3,n4 = 0,0,0,0
    
#     i = 0
#     while i < 4:
#         aux = input(f'Digite o {i+1}º número inteiro: ') 
#         if aux.isnumeric():
#             if n1 == 0:
#                 n1 = int(aux)
#             elif n2 == 0:
#                 n2 = int(aux)
#             elif n3 == 0:
#                 n3 = int(aux)
#             else:
#                 n4 = int(aux)
#             i+=1
#         else:
#             tentativas += 1
#             if tentativas == 3:
#                 print('Número máximo de tentativas alcançado')
#                 quit()
#             print('Favor inserir apenas números inteiros')
#             continue

#     aux = 0
#     if n1 > n2: aux = n1; n1 = n2; n2 = aux
#     if n3 > n4: aux = n3; n3 = n4; n4 = aux
#     if n1 > n3: aux = n1; n1 = n3; n3 = aux
#     if n2 > n4: aux = n2; n2 = n4; n4 = aux 
#     if n2 > n3: aux = n2; n2 = n3; n3 = aux
                
#     print(f'Números Ordenados: {n1} - {n2} - {n3} - {n4}')

while True:
    tentativas = 0
    n1,n2,n3,n4 = 0,0,0,0
    
    i = 0
    while i < 4:
        aux = input(f'Digite o {i+1}º número inteiro: ') 
        if aux.isnumeric():
            if n1 == 0:
                n1 = int(aux)
            elif n2 == 0:
                n2 = int(aux)
            elif n3 == 0:
                n3 = int(aux)
            else:
                n4 = int(aux)
            i+=1
        else:
            tentativas += 1
            if tentativas == 3:
                print('Número máximo de tentativas alcançado')
                quit()
            print('Favor inserir apenas números inteiros')
            continue
    
    while tentativas < 3:
        resp = input('Digite se deseja ordenar em ordem [c]rescente ou [d]ecrescente: ')
        
        aux = 0
        if n1 > n2: aux = n1; n1 = n2; n2 = aux
        if n3 > n4: aux = n3; n3 = n4; n4 = aux
        if n1 > n3: aux = n1; n1 = n3; n3 = aux
        if n2 > n4: aux = n2; n2 = n4; n4 = aux 
        if n2 >  n3: aux = n2; n2 = n3; n3 = aux
            
        if resp == 'c' or resp == '[c]':
            print(f'Números Ordenados de maneira crescente: {n1} - {n2} - {n3} - {n4}')
            break
        elif resp == 'd' or resp == '[d]': 
            print(f'Números Ordenados de maneira decrescente: {n4} - {n3} - {n2} - {n1}')
            break
        else: 
            print(f'Inserir apenas uma das possibilidades')
            tentativas += 1
    else: 
        print('Número máximo de tentativas alcançado')
        quit()