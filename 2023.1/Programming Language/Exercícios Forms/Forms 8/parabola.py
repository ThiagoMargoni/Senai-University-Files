import matplotlib.pyplot as plt
import math
import numpy as np
from os import system
from time import sleep

a,b,c = 0.0, 0.0, 0.0

def verifyNumber(value):
    aux = value.replace(',', '.')
    aux = aux.replace('.', '')
    aux = aux.replace('-', '')

    if aux.isnumeric():
        return float(value)
    else:
        return 'Favor Inserir Apenas Números'

def createParabola(a,b,c):
    delta = b**2 -4*a*c
    
    if delta >= 0:
        x1,x2 = (-b + math.sqrt(delta))/(2*a), (-b - math.sqrt(delta))/(2*a)
    
        xv = -b/(2*a)
        yv = -delta/(4*a)

        x = np.linspace(int(xv)-5, int(xv)+5, 100)
        y = a*x**2 + b*x + c

        plt.plot(x,y)
        plt.axhline(y=0, color='black', linestyle='-')
        plt.axvline(x=0, color='black', linestyle='-')

        plt.plot(x1, 0, marker="o", color='green')
        plt.text(x1-0.5, 2, f'[{round(x1,2)}, 0]',color='green')

        if delta > 0:
            plt.plot(x2, 0, marker="o", color='green')
            plt.text(x2-0.5, 2, f'[{round(x2,2)}, 0]',color='green')

            plt.plot(xv,yv, marker='o', color='blue')
            plt.text(xv-0.5, yv-3.5, f'[{round(xv, 2)}, {round(yv, 2)}]', color='blue')

        plt.show()

    else:
        printar('Delta negativo, impossível calcular')

def printar(value):
    system('cls')
    print(value)
    sleep(2)

while True:
    system('cls')
    aux = verifyNumber(input('Insira o "A": '))
    if type(aux) is not str: a = aux 
    else: printar(aux); continue
    
    system('cls')
    aux = verifyNumber(input('Insira o "B": '))
    if type(aux) is not str: b = aux 
    else: printar(aux); continue

    system('cls')
    aux = verifyNumber(input('Insira o "C": '))
    if type(aux) is not str: c = aux 
    else: printar(aux); continue

    createParabola(a,b,c)