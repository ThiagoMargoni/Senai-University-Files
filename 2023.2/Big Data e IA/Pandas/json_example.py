import numpy as np
import pandas as pd

dados = pd.read_json(path_or_buf="imoveis.json", orient='columns')
dados
dados.ident[0] #Exiba a primeira linha do dataframe
dados.listing[0]#Exiba a primera linha do dataframe

#pré processamento dos dados
#função normalize
dados_lista1 = pd.json_normalize(dados.ident)
dados_lista1.head()#Exibe as primeiras linhas

dados_lista2 = pd.json_normalize(dados.listing, sep='_')
dados_lista2.head()#Exibe as primeiras linhas


dados_imoveis = pd.concat([dados_lista1,dados_lista2], axis=1) # Junta os dataframe

dados_imoveis.head()#Exibe as 4 primeiras linhas do dataframe

print(dados_imoveis.shape)

for coluna in dados_imoveis:
    print("----"*10)
    print(dados_imoveis[coluna].value_counts())
    
#criar um diltro no dataset

filtro = (dados_imoveis['types_usage'] == 'Residencial') & (dados_imoveis['address_city'] == 'Rio de Janeiro')

dados_imoveis = dados_imoveis[filtro] # arnazena o dataset dados_imoveis o filtro cirado na celula de cima

print(dados_imoveis.head())
print(dados_imoveis.info())#retorna as informaçoes do dataset