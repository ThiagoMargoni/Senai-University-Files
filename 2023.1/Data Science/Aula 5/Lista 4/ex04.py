import numpy as np
import matplotlib.pyplot as plt

dict = {
    'temperatura': [21.2,20.3,22.7,22,22.3,23.5,24.8,24.2,25.5,25.2,25.5,25.8,27.5,26.3,28.2,28.6,29,29.7,30.7,30.3,30.2,31.4,32.5,32.7],
    'produtividade': [142,148,131,132,145,138,144,136,141,124,133,128,132,137,124,117,122,131,124,111,119,129,123,116]
}

x = dict['temperatura']
y = dict['produtividade']

matriz_corr = [x, y]
rho = np.corrcoef(matriz_corr)

x_log = []
y_log = []

for i in range(len(x)):
    x_log.append(np.log(x[i]))
    y_log.append(np.log(y[i]))

matriz_corr_log = [x_log, y_log]
rho_log = np.corrcoef(matriz_corr_log)

print(rho)
print(rho_log)

plt.scatter(x, y)
plt.show()

plt.scatter(x_log, y_log)
plt.show()

print('b) Não, o gráfico está totalmente disperso, o que representa que não existe nenhuma relação entre os dados')