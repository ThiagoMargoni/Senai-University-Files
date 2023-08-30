import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('arquivo aqui')
print(dados)

razaoR = []
cont = range(len(dados['amostra']))
for i in cont:
    razaoR.append(dados['d'][i]/dados['h'][i])

matriz_corr = [dados['porca'], dados['h'], dados['d'], dados['m'], razaoR]
rho = np.corrcoef(matriz_corr)

print(rho)

porca_log = []
h_log = []
d_log = []
m_log = []

for i in cont:
    porca_log.append(np.log(dados['porca'][i]))
    h_log.append(np.log(dados['h'][i]))
    d_log.append(np.log(dados['d'][i]))
    m_log.append(np.log(dados['m'][i]))

matriz_corr_log = [porca_log, h_log, d_log, m_log]
rho_lin = np.corrcoef(matriz_corr_log)

print(rho_lin)

alfa = []
beta1 = []
beta2 = []

media_porca = np.average(porca_log)
media_h = np.average(h_log)
media_d = np.average(d_log)

for i in range(len(porca_log)):
    ...