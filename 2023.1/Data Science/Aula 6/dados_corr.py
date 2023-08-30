import numpy as np
import matplotlib.pyplot as plt
import seaborn as snb
import pandas as pd

data = pd.read_csv('./ScienceData/dados_corr.csv')
altura = data['altura']
lado = data['lado']
processo = data['processo']
massa = data['massa']

matriz_corr = [altura,lado,processo,massa]
rho = np.corrcoef(matriz_corr)

altura_log = []
lado_log = []
processo_log = []
massa_log = []

for i in range(len(altura)): 
    altura_log.append(np.log(altura[i]))
    lado_log.append(np.log(lado[i]))
    processo_log.append(np.log(processo[i]))
    massa_log.append(np.log(massa[i]))

matriz_corr_log = [altura_log,lado_log,processo_log,massa_log]
rho_log = np.corrcoef(matriz_corr_log)

print(rho)
print(rho_log) # Linearizado

# mapacalor = snb.heatmap(rho, annot=True)
# plt.grid()

graf_a = plt.scatter(altura, lado)
plt.show()
graf_c = plt.scatter(altura, massa)
plt.show()

graf_a_log = plt.scatter(altura_log, lado_log)
plt.show()
graf_c_log = plt.scatter(altura_log, massa_log)
plt.show()