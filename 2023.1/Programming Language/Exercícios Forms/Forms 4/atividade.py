'''
# Calculadora

resultado = 0

while resultado == 0:
    aux = input("Insira um número qualquer: ")
    aux = aux.replace(".","")
    aux = aux.replace("-","")
    if aux.isdecimal():
        num1 = float(aux)
        aux = input("Insira um outro número qualquer: ")
        aux = aux.replace(".","")
        aux = aux.replace("-","")
        if aux.isdecimal():
            num2 = float(aux)

            aux = input("Por fim insira a operação desejada (* / + -): ")
            if aux == "*" or aux == "/" or aux == "+" or aux == "-":
                match aux:
                    case "*":
                        resultado = num1*num2
                    case "/":
                        if num2 != 0:
                            resultado = num1/num2
                        else:
                            print("\nImpossível dividir qualquer número por 0!\n")
                    case "+":
                        resultado = num1 + num2
                    case "-":
                        resultado = num1-num2
            else: 
                print("\nFavor inserir uma das operações entre parenteses!\n")
        else: 
            print("\nFavor inserir apenas números!\n")
    else: 
        print("\nFavor inserir apenas números!\n")


print(f"O resultado da conta {num1} {aux} {num2} é: {resultado:0.2f}")
# IMC

imc = 0

while imc == 0:
    aux = input("Vamos calcular seu IMC!\nDigite sua altura em metros: ")
    aux = aux.replace(".","")
    aux = aux.replace("-","")
    if aux.isdecimal():
        altura = float(aux)
        aux = input("Agora digite seu peso em KG: ")
        aux = aux.replace(".","")
        aux = aux.replace("-","")
        if aux.isdecimal():
            peso = float(aux)

            imc = peso /(altura**2)

            if imc < 18.5:
                print("\nSeu IMC indica que você está abaixo do peso adequado!")
            elif imc >= 18.5 or imc < 25:
                print("\nSeu IMC indica que você têm o peso normal!")
            elif imc >= 25 or imc < 30:
                print("\nSeu IMC indica que você possui pré obesidade!")
            elif imc >= 30 or imc < 35:
                print("\nSeu IMC indica que você possui obesidade grau 1!")
            elif imc >= 35 or imc < 40:
                print("\nSeu IMC indica que você possui obesidade grau 2!")
            else:
                print("\nSeu IMC indica que você possui obesidade mórbida!")
        else:
            print("\nFavor digitar apenas números!\n")
    else:
        print("\nFavor digitar apenas números!\n")
'''

# Bhaskara

import math

x1 = -1
x2 = 0

while x1 == -1:
    a = input("Insira o valor de A: ")
    b = input("Insira o valor de B: ")
    c = input("Insira o valor de C: ")

    aux = a+b+c
    aux = aux.replace("-","")
    aux = aux.replace(".","")

    if aux.isdecimal():
        a = float(a)
        b = float(b)
        c = float(c)

        delta = b**2 - 4*a*c

        if delta >= 0:
            x1 = (abs(b)+math.sqrt(delta))/2*a
            x2 = (abs(b)-math.sqrt(delta))/2*a
            
            print(f"Resultados:\nx1: {x1}\nx2: {x2}")

        else:
            print("Delta tem um valor negativo, portanto não teremos respostas")
            x1 = 0
    else:
        print("\nFavor digitar apenas números!\n")
'''

# Codificado

codigo = "a"

while codigo != "":
    codigo = input("Digite o valor codificado: ")

    if codigo.isdecimal():
        if len(codigo) == 10:
            zona = int(codigo[0:2])

            match zona:
                case 1: zona = "Sul"
                case 2: zona = "Norte"
                case 3: zona = "Leste"
                case 4: zona = "Oeste"

            temp = int(codigo[2:6])
            temp = str(temp)

            if len(temp) == 4:
                if temp[0:1] == '1':
                    temp = f"-{temp[1:3]},{temp[3:4]}ºC"
                else:
                    temp = f"{temp[0:3]},{temp[3:4]}ºC"
            else:
                temp = f"{temp[0:2]},{temp[2:3]}ºC"

            pluv = int(codigo[6:10])

            print(f"\nRegião: {zona}\nTemperatura: {temp}\nIndice pluviométrico: {pluv}mm\n")
        else:
            print("\nFavor inserir o código com 10 caracteres apenas!\n")
    else:
        print("\nFavor Inserir apenas números!\n")

# Empréstimo

prestacao = 0

while prestacao == 0:
    aux = input("Insira o valor da casa: ")
    aux = aux.replace(".","")
    aux = aux.replace("-","")
    if aux.isdecimal():
        casa = float(aux)
        
        aux = input("Insira o seu salário: ")
        aux = aux.replace(".","")
        aux = aux.replace("-","")

        if aux.isdecimal():
            salario = float(aux)

            aux = input("Digite a quantidade de anos a pagar: ")
            aux = aux.replace(".","")
            aux = aux.replace("-","")

            if aux.isdecimal():
                meses = float(aux)*12

                prestacao = casa/meses
                if prestacao <= (salario*0.3):
                    print("\nParabéns!!!\nVocê conseguirá fazer o empréstimo")
                else:
                    print("\nInfelizmente não será possível fazer o empréstimo!")

            else:
                print("\nFavor Inserir apenas números!\n")

        else:
            print("\nFavor Inserir apenas números!\n")
    else:
        print("\nFavor Inserir apenas números!\n")
'''