# ex 1
lista = []

while True:
    num = input('Insira um número: ')
    aux = num.replace('.', '')

    if aux.isnumeric():
        num = float(num)
        if num >= 0:
            lista.append(num)
        else:
            break
    else:
        break

if len(list) > 0:
    print(f'Lista de números: {lista}') 
else:
    print('Não há nada na Lista')

# ex 2

list = []

i = 0
while i < 5: 
    num = input('Insira um número: ')
    aux = num.replace('-', '')
    aux = aux.replace('.', '')

    if aux.isdecimal():
        num = float(num)
        list.append(num)
        i+=1        
    else:
        print('Favor inserir apenas números')

while True: 
    aux = input('Dejesa ordenar por ordem [c]rescente ou [d]ecrescente? ')

    if aux == 'c' or aux == 'crescente':
        print(f'Crescente: {sorted(list)}')
        break
    elif aux == 'd' or aux == 'decrescente':
        print(f'Decrescente: {sorted(list, reverse=True)}')
        break
    else: 
        print('Favor inserir apenas uma das duas opções')

# ex 3

lista1, lista2 = [], []
while True:
    num = input(f'Insira um número para a {1 if len(lista1) < 5 else 2}ª lista: ')
    aux = num.replace('-', '')
    aux = aux.replace('.', '')

    if aux.isdecimal():
        num = float(num)
        if len(lista1) < 5:
            lista1.append(num)

        elif len(lista2) < 5:
            lista2.append(num)
            
            if len(lista2) == 5:
                break
    else:
        print('Favor inserir apenas números')

listaSoma, listaMaior, listaMenor = [],[],[]

for i in range(len(lista1)):
    listaSoma.append((lista1[i]+lista2[i]))

    if lista1[i] >= lista2[i]: listaMaior.append(lista1[i])
    else: listaMaior.append(lista2[i])

    if lista1[i] <= lista2[i]: listaMenor.append(lista1[i])
    else: listaMenor.append(lista2[i])

listaDuplicados = []

def verificarContem(num):
    if not num in listaDuplicados:
        listaDuplicados.append(num)

for i in range(len(lista1)):
    if lista1[i] == lista2[i] or lista1[i] == listaSoma[i] or lista1[i] == listaMaior[i] or lista1[i] == listaMenor[i]:
        verificarContem(lista1[i])

    elif lista2[i] == listaSoma[i] or lista2[i] == listaMaior[i] or lista2[i] == listaMenor[i]:
        verificarContem(lista2[i])

    elif listaSoma[i] == listaMaior[i] or listaSoma[i] == listaMenor[i]: 
        verificarContem(listaSoma[i])

    elif listaMaior[i] == listaMenor[i]: 
        verificarContem(listaMaior[i])

if len(listaDuplicados) > 0:
    print(f'Total de repetições: {len(listaDuplicados)} e os números repetidos são: {listaDuplicados}')
else: 
    print('Não há repetições em nenhuma tabela')

# ex 4

listaGeral = [[0, "", False, 0.0], ("a", 1), {"a": "b", "c": "d"}, 2.565, "sasa", 29382, False, True, "ahdshda", 498248723, [False, 312, "", 321321], {"b": 2, "a": 1},
              ("b", 2), 324324.232]
listBool, listString, listInt, listFloat, listDict, listList, listTuple = [], [], [], [], [], [], []

for i in range(len(listaGeral)):
    if type(listaGeral[i]) == bool:
        listBool.append(listaGeral[i])
    
    elif type(listaGeral[i]) == str:
        listString.append(listaGeral[i])
    
    elif type(listaGeral[i]) == int:
        listInt.append(listaGeral[i])
    
    elif type(listaGeral[i]) == float:
        listFloat.append(listaGeral[i])

    elif type(listaGeral[i]) == dict:
        listDict.append(listaGeral[i])

    elif type(listaGeral[i]) == list:
        listList.append(listaGeral[i])

    elif type(listaGeral[i]) == tuple:
        listTuple.append(listaGeral[i])
    
    else:
        print('Não sei o tipo')

print(f'Lista de Bool:')
print(*listBool, sep='\n')

print('\nLista de String:')
print(*listString, sep='\n')

print('\nLista de Int:')
print(*listInt, sep='\n')

print('\nLista de Float:')
print(*listFloat, sep='\n')

print('\nLista de Dict:')
print(*listDict, sep='\n')

print('\nLista de Listas:')
print(*listList, sep='\n')

print('\nLsta de Tuplas:')
print(*listTuple, sep='\n')
