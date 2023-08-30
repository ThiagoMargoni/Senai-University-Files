import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

arquivo = r'C:/Users/dsadm/Downloads/dados_seguros/dados_seguros.csv'
dados_originais = pd.read_csv(arquivo, header=1)

dados = dados_originais.to_dict('list')

q1 = np.percentile(dados["Fatia de Mercado"], 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados["Fatia de Mercado"], 75, method="averaged_inverted_cdf")
dq = q3 - q1

lim_inf = np.fmax(min(dados["Fatia de Mercado"]), q1 - 1.5*dq)
lim_sup = np.fmin(max(dados["Fatia de Mercado"]), q3 + 1.5*dq)
tamanho = len(dados["Fatia de Mercado"])           

diagrama = plot.boxplot(dados["Fatia de Mercado"])
plot.title("boxplot dos dados de seguro !!!")
plot.ylabel("Fatia de merdado (%)")
plot.show()