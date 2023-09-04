import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

vazao = np.array([10,20,30,5,35,40]).reshape(-1, 1)
nivel = np.array([50, 60, 70, 45, 80, 85]).reshape(-1, 1)

model = LinearRegression()
model.fit(vazao, nivel)

vazao_teste = np.array([51,22,47,6,8]).reshape(-1, 1)

nivel_previsto = model.predict(vazao_teste)

for i in range(len(vazao_teste)):
    print(f'Vazão: {vazao_teste[i][0]} - Nível Previsto: {nivel_previsto[i]}')

plt.scatter(vazao, nivel, color='blue', label='Dados de Treinamento')
plt.plot(vazao_teste, nivel_previsto, color='red', label='Dados de Teste')
plt.xlabel('Vazão da Água (m3/min)')
plt.ylabel('Nível de Tanque (metros)')
plt.title('Relação entre vazão de água e nível do tanque')
plt.legend()
plt.grid(True)
plt.show()