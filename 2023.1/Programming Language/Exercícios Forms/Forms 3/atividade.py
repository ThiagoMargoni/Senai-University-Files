# tempo perdido cigarros

cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = float(input("Há quantos anos você fuma? "))

total_dias = anos * 365

min_perdido = total_dias * cigarros * 10

print(f"Você perdeu aproximadamente um total de {min_perdido/1440} dias na sua vida")

# 3 números

a = int(input("Digite um Número inteiro: \n"))
b = int(input("Digite outro Número inteiro: \n"))
c = int(input("Digite mais um Número inteiro: \n"))

print(f"A soma dos quadrados desses números é: {a**2 + b**2 + c**2}")

# conversor de metros

metros = float(input("Digite o valor em metros que deseja converter: \n"))

print(f"Milímetros: {metros*1000} mm \nCentímetros: {metros*100} cm \nDecimetros: {metros*10} dm \nQuilômetros: {metros/1000} km")

# calcular total segundos

dias = int(input("Insira o total de dias: "))
horas = int(input("Insira o total de horas: "))
minutos = int(input("Insira o total de minutos: "))
segundos = int(input("Insira o total de segundos: "))

print(f"Todos os valores escritos somados resultam em um total de {(dias*86400) + (horas*3600) + (minutos*60) + segundos} segundos")

# calcular desconto produto

valor = float(input("Digite o valor do produto: "))
porcentagem = float(input("Digite a porcentagem do desconto: "))

desconto = valor*(porcentagem/100)

print(f"Você receberá um total de R${desconto} de desconto, tendo que pagar R${valor - desconto}")

# calcular aumento de salário

valor = float(input("Digite o valor do salário atual: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))

aumento = valor*(porcentagem/100)

print(f"Você receberá um aumento de R${aumento}, tendo como novo salário R${valor + aumento}")

# trocar A e B

a = int(input("Digite um Número: "))
b = int(input("Digite outro Número: "))

aux1 = a
aux2 = b

a = aux2
b = aux1

print(f"O valor antigo de A era {aux1} e passou a ser {a}\nO mesmo ocorreu com o B, que tinha como valor {aux2} e agora é {b}")

# carro alugado

dias = int(input("Insira o total de dias pelos quais o carro foi alugado: "))
km = float(input("Insira o total de km percorridos: "))

print(f"O valor total a ser pago será de R${(dias*60)+(km*0.15)}")

# antecessor e sucessor

num = int(input("Insira um número inteiro: "))

print(f"O sucessor desse número é o {num+1} e o antecessor é {num-1}")

# eleição sindical

qtd = int(input("Quantidade total de eleitores: "))
A = 0
B = 0
C = 0
nulo = 0
branco = 0

for x in range(qtd):
    resp = int(input("\nDigite em quem deseja votar: \n1 = A\n2 = B\n3 = C\n4 = Nulo\n5 = Branco\n-----------------------\n"))

    match resp:
        case 1:
            A+=1
        case 2:
            B+=1
        case 3:
            C+=1
        case 4:
            nulo+=1
        case 5:
            branco+=1

votosValidos = A + B + C

print(f"\nAo todo tivemos {qtd} eleitores.\nO candidato A teve um total de {(A/votosValidos)*100}% de votos válidos.\nO candidato B teve um total de {(B/votosValidos)*100}% de votos válidos.\nO candidato C teve um total de {(C/votosValidos)*100}% de votos válidos.\nPara finalizar tivemos um total de {(nulo/qtd)*100}% votos nulos e {(branco/qtd)*100}% de votos brancos\n")