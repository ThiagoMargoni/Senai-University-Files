import numpy as np
import matplotlib.pyplot as plot

dados = [45, 56, -89, 23.4, 1.5, 2.5, 5.5, 10, -50, 1]
dados.append(-12.5)
dados.sort()

Q1 = np.percentile(dados, 25)
Q2 = np.percentile(dados, 50)
Q3 = np.percentile(dados, 75)

dq = Q3 - Q1

lower_limit = np.fmax(dados[0], Q1 - 1.5*dq)
upper_limit = np.fmin(dados[-1], Q3 + 1.5*dq)

diagram = plot.boxplot(dados, labels=["X"], positions=[1])

dados_sem = dados

for i in dados_sem:
    if i < lower_limit or i > upper_limit:
        dados_sem.remove(i)

Q1 = np.percentile(dados_sem, 25)
Q2 = np.percentile(dados_sem, 50)
Q3 = np.percentile(dados_sem, 75)

dq = Q3 - Q1

lower_limit = np.fmax(dados_sem[0], Q1 - 1.5*dq)
upper_limit = np.fmin(dados_sem[-1], Q3 + 1.5*dq)

diagram = plot.boxplot(dados_sem, labels=["Y"], positions=[2])

plot.title("Title")
plot.show()