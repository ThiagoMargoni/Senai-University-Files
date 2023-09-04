import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

A = np.array([50,100,120,300]).reshape(-1, 1)
valor = np.array([180000, 300000, 375000, 600000]).reshape(-1, 1)

model = LinearRegression()
model.fit(A, valor)

A_teste = np.array([253, 321, 312, 920]).reshape(-1, 1)

valor_previsto = model.predict(A_teste)

for i in range(len(A_teste)):
    print(f'Área: {A_teste[i][0]} - Valor Previsto: {valor_previsto[i]}')

plt.scatter(A, valor, color='blue', label='Dados de Treinamento')
plt.plot(A_teste, valor_previsto, color='red', label='Dados de Teste')
plt.xlabel('Área do Terreno (m²)')
plt.ylabel('Valor do Terreno (em milhões de reais)')
plt.title('Relação entre área do terreno e preço do terreno')
plt.legend()
plt.grid(True)
plt.show()