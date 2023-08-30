# exercício 1

# tentativas = 0
# while tentativas < 3:

#     aux = input("Insira um número qualquer ou digite 'sair' para finalizar o programa: ")
#     aux = aux.replace(".","")
#     aux = aux.replace("-","")
#     if aux.isdecimal():
#         num1 = float(aux)
#         aux = input("Insira um outro número qualquer: ")
#         aux = aux.replace(".","")
#         aux = aux.replace("-","")
#         if aux.isdecimal():
#             num2 = float(aux)

#             aux = input("Por fim insira a operação desejada (* / + -): ")
#             if aux == "*" or aux == "/" or aux == "+" or aux == "-":
#                 match aux:
#                     case "*":
#                         print(f'\nResultado: {num1*num2}')
#                     case "/":
#                         if num2 != 0:
#                             print(f'\nResultado: {num1/num2}')
#                         else:
#                             print("\nImpossível dividir qualquer número por 0!\n")
#                             tentativas += 1
#                     case "+":
#                         print(f'\nResultado: {num1+num2}')
#                     case "-":
#                         print(f'\nResultado: {num1-num2}')
#             else: 
#                 if aux == 'sair':
#                     quit()
#                 else:
#                     print("\nFavor inserir uma das operações entre parenteses!\n")
#                     tentativas += 1
#         else:
#             if aux == 'sair':
#                 quit()
#             else:
#                 print("\nFavor inserir apenas números!\n")
#                 tentativas += 1
            
#     else:
#         if aux == 'sair':
#             quit()
#         else:
#             print("\nFavor inserir apenas números!\n")
#             tentativas += 1
# print('Programa finalizado por erro máximo de tentativas alcançadas!')

# exercício 2

# tentativas = 0
# while tentativas < 3:

#     altura = input("Digite sua altura em metros ou digite 'sair' para finalizar o programa: ")
#     aux = altura.replace(".","")
#     aux = aux.replace("-","")
#     if aux.isdecimal():
#         altura = float(altura)
#         peso = input("Agora digite seu peso em KG: ")
#         aux = peso.replace(".","")
#         aux = aux.replace("-","")
#         if aux.isdecimal():
#             peso = float(peso)

#             imc = peso /(altura**2)

#             if imc < 18.5:
#                 print("\nSeu IMC indica que você está abaixo do peso adequado!")
#             elif imc >= 18.5 and imc < 25:
#                 print("\nSeu IMC indica que você têm o peso normal!")
#             elif imc >= 25 and imc < 30:
#                 print("\nSeu IMC indica que você possui pré obesidade!")
#             elif imc >= 30 and imc < 35:
#                 print("\nSeu IMC indica que você possui obesidade grau 1!")
#             elif imc >= 35 and imc < 40:
#                 print("\nSeu IMC indica que você possui obesidade grau 2!")
#             else:
#                 print("\nSeu IMC indica que você possui obesidade mórbida!")
#         else:
#             if aux == 'sair':
#                 quit()
#             else:
#                 print("\nFavor inserir apenas números!\n")
#                 tentativas += 1
#     else:
#         if aux == 'sair':
#             quit()
#         else:
#             print("\nFavor inserir apenas números!\n")
#             tentativas += 1
# print('Programa finalizado por erro máximo de tentativas alcançadas!')

# exercício 3

import math 

def verificarDecimal(x):
    global tentativas
    aux = x.replace('-', '')
    aux = aux.replace('.', '')
    if not aux.isdecimal():
        if x == 'sair':
            quit()
        else:
            print("\nFavor digitar apenas números!\n")
            tentativas += 1
            return False
            

tentativas = 0
while tentativas < 3:

    a = input("Insira o valor de A ou 'sair' para finalizar o programa: ")
    if verificarDecimal(a) == False: 
        continue
    b = input("Insira o valor de B: ")
    if verificarDecimal(b) == False: 
        continue
    c = input("Insira o valor de C: ")
    if verificarDecimal(c) == False: 
        continue

    a = float(a)
    b = float(b)
    c = float(c)

    delta = b**2 - 4*a*c

    if delta >= 0:
        x1 = (abs(b)+math.sqrt(delta))/2*a
        x2 = (abs(b)-math.sqrt(delta))/2*a
            
        print(f"\nResultados:\nx1: {x1}\nx2: {x2}")

    else:
        print("\nDelta tem um valor negativo, portanto não teremos respostas") 

print('Programa finalizado por erro máximo de tentativas alcançadas!')


# exercício 4

tentativas = 0
while tentativas < 3:
    codigo = input("Digite o valor codificado ou 'sair' para finalizar o programa: ")

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

            if temp[0:1] == '1':
                temp = f"-{temp[1:3]},{temp[3:4]}ºC"
            else:
                temp = f"{temp[0:2]},{temp[2:3]}ºC"

            pluv = int(codigo[6:10])

            print(f"\nRegião: {zona}\nTemperatura: {temp}\nIndice pluviométrico: {pluv}mm\n")
        else:
            print("\nFavor inserir o código com 10 caracteres apenas!\n")
            tentativas+=1
    else:
        if codigo == 'sair':
            quit()
        else:
            print("\nFavor Inserir apenas números!\n")
            tentativas+=1

print('Programa finalizado por erro máximo de tentativas alcançadas!')


#exercício 5

tentativas = 0

while tentativas < 3:
    aux = input("Insira o valor da casa ou digite 'sair' para finalizar o programa: ")
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
                if aux == 'sair':
                    quit()
                else:
                    print("\nFavor Inserir apenas números!\n")
                    tentativas += 1
        else:
            if aux == 'sair':
                quit()
            else:
                print("\nFavor Inserir apenas números!\n")
                tentativas+=1
    else:
        if aux == 'sair':
            quit()
        else:
            print("\nFavor Inserir apenas números!\n")
            tentativas+=1

print('Programa finalizado por erro máximo de tentativas alcançadas!')