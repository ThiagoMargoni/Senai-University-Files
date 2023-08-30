import matplotlib.pyplot as plot
import numpy as np

data = {
    'session': ['Pessoal', 'Pessoal', 'Pessoal', 'Pessoal', 'Pessoal', 'Pessoal', 'Pessoal', 'Técnica', 'Técnica', 'Técnica', 'Técnica', 'Técnica', 'Técnica', 'Técnica', 'Vendas', 
                'Vendas', 'Vendas', 'Vendas', 'Vendas', 'Vendas', 'Vendas', 'Vendas', 'Vendas', 'Vendas', 'Vendas'],
    'right': [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    'politic': [9.0, 6.5, 9.0, 6.0, 6.5, 6.5, 9.0, 6.0, 9.0, 9.0, 7.0, 5.5, 6.0, 8.0, 7.0, 9.0, 10.0, 5.5, 7.0, 6.0, 6.5, 6.0, 9.0, 6.5, 7.0],
    'statistic': [9, 9, 8, 8, 9, 10, 8, 8, 9, 8, 10, 7, 7, 9, 8, 7, 8, 9, 2, 7, 7, 8, 9, 8, 7],
    'average': []
}

listAveragePessoal, listAverageTecnica, listAverageVendas = [], [], []

def organizeAverage():
    for x in range(len(data['session'])):
        data['average'].append(np.average([data['right'][x], data['politic'][x], data['statistic'][x]]))

    for x in range(len(data['session'])):
        if data['session'][x] == 'Pessoal':
            listAveragePessoal.append(data['average'][x])

        elif data['session'][x] == 'Técnica':
            listAverageTecnica.append(data['average'][x])
        
        else:
            listAverageVendas.append(data['average'][x])



def boxplot(list, label, pos):

    list.sort()

    Q1 = np.percentile(list, 25, method="averaged_inverted_cdf")
    Q2 = np.percentile(list, 50, method="averaged_inverted_cdf")
    Q3 = np.percentile(list, 75, method="averaged_inverted_cdf")

    dq = Q3 - Q1

    lower_limit = np.fmax(list[0], Q1 - 1.5*dq)
    upper_limit = np.fmin(list[-1], Q3 + 1.5*dq)

    diagram = plot.boxplot(list, labels=[label], positions=[pos])

    print(f'\n-------------------{label}----------------------\nAverage: {np.average(list):.1f}\nMedian: {Q2:.1f}\nStandart Deviation: {np.std(list):.1f}')

organizeAverage()

plot.figure(figsize=(12,8))

boxplot(data['right'], "Right", 1)
boxplot(data['politic'], "Politic", 2)
boxplot(data['statistic'], "Statistic", 3)

boxplot(listAveragePessoal, 'Average Pessoal', 4)
boxplot(listAverageTecnica, 'Average Técnica', 5)
boxplot(listAverageVendas, 'Average Vendas', 6)
boxplot(data['average'], 'Average All Class', 7)

plot.title("Training Data")
plot.ylabel("Grade")
plot.show()