import numpy as np
import matplotlib.pyplot as plt

dados = {
    'peso': [30,32,24,28,26,34,25,23,35,31],
    'altura': [145,150,125,140,127,145,132,112,155,145]
}

alfa = []
beta = []
media_peso = np.average(dados['peso'])
media_altura = np.average(dados['altura'])

for i in range(len(dados['peso'])):

    alfa.append(dados['peso'][i]-media_peso)
    beta.append(dados['altura'][i]-media_altura)

soma_numerador = 0.0
soma_denominador = 0.0

for i in range(len(alfa)):
    soma_numerador += alfa[i]*beta[i]
    
    soma_denominador += alfa[i]**2

a = soma_numerador/soma_denominador
b = media_altura - (a * media_peso)

pesos = [5,10,15,20,25,30,35,40,45,50]
altura_prevista = []
for i in range(len(pesos)):    
    altura_prevista.append(a * pesos[i] + b)

soma_residuos = 0.0
denomidor_residuo = 0.0
for i in range(len(dados['peso'])):
    soma_residuos += (dados['altura'][i] - (a*dados['peso'][i]+b))**2

    denomidor_residuo += beta[i]**2

r2 = 1 - soma_residuos/denomidor_residuo
print(r2)

graf1 = plt.scatter(dados['peso'], dados['altura'])
graf2 = plt.plot(pesos, altura_prevista)

plt.title('Altura em função do peso')
plt.xlabel('Peso')
plt.ylabel('Altura')
plt.show()