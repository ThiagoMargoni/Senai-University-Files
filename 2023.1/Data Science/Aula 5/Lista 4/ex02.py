import numpy as np
import matplotlib.pyplot as plt

dict = {
    'num_erros': [6,8,6,10,8,14,12,14,12,16],
    'num_horas': [8,8,12,12,16,16,20,20,24,24]
}

x = dict['num_erros']
y = dict['num_horas']

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

graf = plt.scatter(x, y)
plt.show()

graf_log = plt.scatter(x_log, y_log)
plt.show()

print('Inicialmente pensei que haveria alguma relação, porém ao analisar esses dados especificamente percebe-se que' + 
      ', o gráfico está totalmente disperso, o que representa que não existe nenhuma relação entre os dados')