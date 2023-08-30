import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'C:/Users/MTA6CA/Documents/BoschFiles/Python/HomeWork/Ciencia Dados/List 4/dados_imposto_empresa.csv')

qtd_dados = len(data['Empresa'])
k = 1 + 3.32 * np.log10(qtd_dados)
k = np.round(k)

qtd, classes = np.histogram(data['Imposto (%)'], bins=int(k))

diagram = plt.hist(data['Imposto (%)'], bins=int(k))
plt.show()