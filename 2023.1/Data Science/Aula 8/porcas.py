import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv(r'C:/Users/dsadm/Downloads/A/porcas.csv', sep=';')

razaoR, razaoK = [], []
cont = range(len(dados['amostra']))
for i in cont:
    razaoR.append(dados['d'][i]/dados['h'][i])

    razaoK.append(dados['d'][i]*dados['h'][i])

matriz_corr = [dados['porca'], dados['h'], dados['d'], dados['m'], razaoR, razaoK]
rho = np.corrcoef(matriz_corr)

porca_log = []
h_log = []
d_log = []
m_log = []
razaoK_log = []

for i in cont:
    porca_log.append(np.log(dados['porca'][i]))
    h_log.append(np.log(dados['h'][i]))
    d_log.append(np.log(dados['d'][i]))
    m_log.append(np.log(dados['m'][i]))
    razaoK_log.append(np.log(razaoK[i]))

matriz_corr_log = [porca_log, h_log, d_log, m_log, razaoK_log]
rho_lin = np.corrcoef(matriz_corr_log)

alfa = []
beta1 = []
beta2 = []

alfa_k = []
beta_massa = []

media_porca = np.average(dados['porca'])
media_h = np.average(dados['h'])
media_d = np.average(dados['d'])
media_massa = np.average(dados['m'])
media_k = np.average(razaoK)

for i in cont:
    alfa.append(dados['porca'][i]-media_porca)
    beta1.append(dados['h'][i]-media_h)
    beta2.append(dados['d'][i]-media_d)

    alfa_k.append(razaoK[i]-media_k)
    beta_massa.append(dados['m'][i]-media_massa)

soma_numerador_porca_h = 0.0
soma_numerador_porca_d = 0.0
soma_denominador = 0.0

soma_numerador_massa_k = 0.0
soma_denominador_k = 0.0

for i in cont:
    soma_numerador_porca_h += alfa[i]*beta1[i]
    soma_numerador_porca_d += alfa[i]*beta2[i]
    soma_denominador += alfa[i]**2

    soma_numerador_massa_k += alfa_k[i]*beta_massa[i]
    soma_denominador_k += alfa_k[i]**2

a_h = soma_numerador_porca_h/soma_denominador
b_h = media_h - (a_h*media_porca)

a_d = soma_numerador_porca_d/soma_denominador
b_d = media_d - (a_d*media_porca)

a_k = soma_numerador_massa_k/soma_denominador_k
b_k = media_massa - (a_k*media_k)

porcas = [4,5,8,10,12,14,18,20,24,27,30]
h_previsto, d_previsto, massa_prevista = [], [], []
for i in range(len(porcas)):
    h_previsto.append(a_h*porcas[i]+b_h)
    d_previsto.append(a_d*porcas[i]+b_d)
    massa_prevista.append(a_k*(h_previsto[i]*d_previsto[i])+b_k)

print(massa_prevista)

graf_h_real = plt.scatter(dados['porca'], dados['h'])
graf_h_modelo = plt.scatter(porcas, h_previsto)
plt.show()

graf_d_real = plt.scatter(dados['porca'], dados['d'])
graf_d_modelo = plt.scatter(porcas, d_previsto)
plt.show()

soma_residuos_h = 0.0
denomidor_residuo_h = 0.0

soma_residuos_d = 0.0
denomidor_residuo_d = 0.0

for i in cont:
    soma_residuos_h += (dados['h'][i] - (a_h*dados['porca'][i]+b_h))**2
    denomidor_residuo_h += beta1[i]**2

    soma_residuos_d += (dados['d'][i] - (a_d*dados['porca'][i]+b_d))**2
    denomidor_residuo_d += beta2[i]**2

r2_h = 1 - soma_residuos_h/denomidor_residuo_h
r2_d = 1 - soma_residuos_d/denomidor_residuo_d