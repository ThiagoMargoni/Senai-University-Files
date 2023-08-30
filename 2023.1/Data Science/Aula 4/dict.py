import numpy as np
import matplotlib.pyplot as plot

dados = {"Ramos" : ["Auto", "Saúde", "incêndio", "vida", "Riscos diversos",
         "Habitação", "transporte", "Acidente Pessoais", "Obrigatório Veículos"
         "Riscos de Engenharia", "Responsabilidade Civil"],
          "%" : [33.6, 14, 12.9, 12.2, 5.5, 3.1, 2.9, 1.7, 1, 0.9]}

q1 = np.percentile(dados["%"], 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados["%"], 75, method="averaged_inverted_cdf")
dq = q3 - q1

lim_inf = np.fmax(min(dados["%"]), q1 - 1.5*dq)
lim_sup = np.fmin(max(dados["%"]), q3 + 1.5*dq)
tamanho = len(dados["%"])          
contador = range(tamanho)          

for i in contador:                  
    if((dados["%"][i] > lim_sup or (dados["%"][i]) < lim_inf)):
        print("Outlier: ", dados["Ramos"][i], ' - ', dados['%'][i])
    else:
        print("Valores não outlier de 1 =", i)


diagrama = plot.boxplot(dados["%"])
plot.title("boxplot dos dados de seguro !!!")
plot.ylabel("Fatia de merdado (%)")
plot.show()