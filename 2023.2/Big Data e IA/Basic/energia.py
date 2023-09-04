import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

demanda = np.array([100, 200, 80, 100, 160]).reshape(-1, 1)
consumo = np.array([50, 140, 30, 75, 123]).reshape(-1, 1)

model = LinearRegression()
model.fit(demanda, consumo)

demanda_teste = np.array([30, 230, 300, 180, 100]).reshape(-1, 1)

consumo_previsto = model.predict(demanda_teste)

for i in range(len(demanda_teste)):
    print(f'Demanda: {demanda_teste[i][0]} - Consumo Previsto: {consumo_previsto[i]}')

plt.scatter(demanda, consumo, color='blue', label='Dados de Treinamento')
plt.plot(demanda_teste, consumo_previsto, color='red', label='Dados de Teste')
plt.xlabel('Demanda (KW)')
plt.ylabel('Consumo (KW)')
plt.title('Relação entre a demanda e os gastos de energias')
plt.legend()
plt.grid(True)
plt.show()