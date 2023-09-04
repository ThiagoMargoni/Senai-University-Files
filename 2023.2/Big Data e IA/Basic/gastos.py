import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

salario = np.array([1200,5000,8000,10000, 30000]).reshape(-1, 1)
gastos = np.array([750, 1500, 4000, 6000, 18000]).reshape(-1, 1)

model = LinearRegression()
model.fit(salario, gastos)

salario_teste = np.array([214214, 15000, 20000, 100000, 6000]).reshape(-1, 1)

gastos_previstos = model.predict(salario_teste)

for i in range(len(salario_teste)):
    print(f'Área: {salario_teste[i][0]} - Gasto Previsto: {gastos_previstos[i]}')

plt.scatter(salario, gastos, color='blue', label='Dados de Treinamento')
plt.plot(salario_teste, gastos_previstos, color='red', label='Dados de Teste')
plt.xlabel('Salário (em reais)')
plt.ylabel('Gastos (em reais)')
plt.title('Relação entre o salário ganho e os gastos')
plt.legend()
plt.grid(True)
plt.show()