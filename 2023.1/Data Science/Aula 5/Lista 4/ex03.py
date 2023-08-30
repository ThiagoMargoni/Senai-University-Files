import numpy as np
import matplotlib.pyplot as plt

dict = {
    'unidade': [40,60,80,100,120,140,160],
    'rendimento': [15.9,18.8,21.6,25.2,28.7,30.4,30.7]
}

x = dict['unidade']
y = dict['rendimento']

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