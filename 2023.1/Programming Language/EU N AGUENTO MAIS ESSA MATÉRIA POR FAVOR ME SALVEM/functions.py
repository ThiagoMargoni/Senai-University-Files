from pick import pick
from tabulate import tabulate
from os import system
from time import sleep

def inputer(value):
    system('cls')
    return input(value)

def printer(value):
    system('cls')
    print(value)
    sleep(2)

def tabulater(list, type):
    printer(tabulate(list, tablefmt=type))

def generateCard():
    list = []
    num = 0

    for i in range(1, 7):
        list2 = []
        for x in range(10):
            list2.append(x*i)
        list.append(list2)

    return list

def verifyNumber(number):
    if number.isdecimal():
        return int(number)
    else:
        return 'Inserir apenas números inteiros'

def createPick(title, options):
    
    option, index = pick(options, title, indicator='->', default_index=0)
    
    return option, index

tabulater(generateCard(), 'fancy_grid')
printer(verifyNumber(input('Insira um número')))