import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

arquivo = r'C:/Users/dsadm/Downloads/dados_seguros/dados_pop.csv'
dados_originais = pd.read_csv(arquivo, header=1)

dados = dados_originais.to_dict('list')

q1 = np.percentile(dados["População"], 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados["População"], 75, method="averaged_inverted_cdf")
dq = q3 - q1

lim_inf = np.fmax(min(dados["População"]), q1 - 1.5*dq)
lim_sup = np.fmin(max(dados["População"]), q3 + 1.5*dq)

diagrama = plot.boxplot(dados["População"], labels=['Brasil Inteiro'], positions=[1])

dados_sudeste = {'Município': [], 'População': []}

for x in range(int(len(dados['Município']))):
    if dados['Estado'][x] == 'SP' or dados['Estado'][x] == 'RJ' or dados['Estado'][x] == 'BH' or dados['Estado'][x] == 'ES':
        dados_sudeste['Município'].append(dados['Município'][x])
        dados_sudeste['População'].append(dados['População'][x])

q1 = np.percentile(dados_sudeste["População"], 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados_sudeste["População"], 75, method="averaged_inverted_cdf")
dq = q3 - q1

lim_inf = np.fmax(min(dados_sudeste["População"]), q1 - 1.5*dq)
lim_sup = np.fmin(max(dados_sudeste["População"]), q3 - 1.5*dq)

diagrama = plot.boxplot(dados_sudeste["População"], labels=['Sudeste Apenas'], positions=[2])

# tupla_exemplo = [('campinas', 1000), ('piracicaba', 100)]
contador = range(len(dados['Município']))
tupla_nordeste = list(zip()) 

estados_nordeste = ['BA', 'SE', 'AL', 'CE', 'RN', 'MA', 'PE', 'PI', 'PB']

for i in contador:
    if(dados['Estado'][i] in estados_nordeste):
        t = (dados['População'][i], dados['Município'][i])
        tupla_nordeste.append(t)

tupla_nordeste.sort()

print(tupla_nordeste[0], tupla_nordeste[1], tupla_nordeste[2])

plot.title("Box Plot dos Estados")
plot.ylabel("População")
plot.show()