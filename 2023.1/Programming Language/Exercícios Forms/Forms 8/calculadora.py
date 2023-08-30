from pick import pick
from os import system
from time import sleep

n1, n2, operation = 0.0, 0.0, ''

def createPick(options, title):
    system('cls')
    option, index = pick(options=options, title=title, indicator='->')

    return option, index

def calculate(n1, n2, operation):
    
    try:
        result = n1+n2 if operation == '+' else n1-n2 if operation == '-' else n1*n2 if operation == '*' else n1/n2
        return f'O resultado da conta é: {round(result, 2)}'
    except ZeroDivisionError: 
        return 'Erro: Favor não tentar dividir o valor por zero'
    except:
        return 'Ocorreu um Erro'
    
def verifyNumber(value):
    value = value.replace(',', '.')
    value = value.replace('.', '')
    value = value.replace('-', '')

    if value.isnumeric():
        return float(value)
    else:
        return 'Favor Inserir Apenas Números'

def printar(value):
    system('cls')
    print(value)
    sleep(2)

while True:
    system('cls')
    aux = verifyNumber(input('Insira o Primeiro número: '))
    if type(aux) is not str: n1 = aux 
    else: printar(aux); continue
    
    system('cls')
    aux = verifyNumber(input('Insira o Segundo número: '))
    if type(aux) is not str: n2 = aux 
    else: printar(aux); continue

    opt, idx = createPick(['+', '-', '*', '/'], 'Selecione a Operação desejada')

    printar(calculate(n1,n2,opt))