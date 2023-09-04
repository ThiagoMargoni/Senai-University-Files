import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

Q = np.array([100,200,300,400,500,600,700]).reshape(-1, 1)
T = np.array([30, 35, 40, 45, 60, 100, 150]).reshape(-1, 1)

model = LinearRegression()
model.fit(Q, T)

Q_teste = np.array([253, 321, 312, 920, 675, 888, 1000]).reshape(-1, 1)

T_previsto = model.predict(Q_teste)

for i in range(len(Q_teste)):
    print(f'Quantidade de Calor: {Q_teste[i][0]} - Temperatura Prevista: {T_previsto[i]}')

plt.scatter(Q, T, color='blue', label='Dados de Treinamento')
plt.plot(Q_teste, T_previsto, color='red', label='Dados de Teste')
plt.xlabel('Quantidade de Calor')
plt.ylabel('Temperatura (ºC)')
plt.title('Relação entre quantidade de calor e temperatura')
plt.legend()
plt.grid(True)
plt.show()