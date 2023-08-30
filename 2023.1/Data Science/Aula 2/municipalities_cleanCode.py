import numpy as np
import matplotlib.pyplot as plot

all_municipalities = [{"state": "SP","pop": 988.8},
                      {"state": "RJ","pop": 556.9},
                      {"state": "BA","pop": 224.6},
                      {"state": "MG","pop": 210.9},
                      {"state": "CE","pop": 201.5},
                      {"state": "DF","pop": 187.7},
                      {"state": "PR","pop": 151.6},
                      {"state": "PE","pop": 135.8},
                      {"state": "RS","pop": 129.9},
                      {"state": "AM","pop": 119.4},
                      {"state": "PA","pop": 116.0},
                      {"state": "GO","pop": 102.3},
                      {"state": "SP","pop": 101.8},
                      {"state": "SP","pop": 92.4},
                      {"state": "RJ","pop": 84.7},
                      {"state": "RJ","pop": 83.9},
                      {"state": "MA","pop": 80.2},
                      {"state": "AL","pop": 74.7},
                      {"state": "RJ","pop": 72.7},
                      {"state": "SP","pop": 68.4},
                      {"state": "RN","pop": 66.8},
                      {"state": "PI","pop": 66.8},
                      {"state": "SP","pop": 63.7},
                      {"state": "SP","pop": 62.8},
                      {"state": "MS","pop": 61.9},
                      {"state": "PB","pop": 56.2},
                      {"state": "PE","pop": 54.1},
                      {"state": "MG","pop": 50.3},
                      {"state": "SP","pop": 49.7},
                      {"state": "SP","pop": 46.3}]

def boxplot(list, label, pos):

    list.sort()

    Q1 = np.percentile(list, 25, method="averaged_inverted_cdf")
    Q2 = np.percentile(list, 50, method="averaged_inverted_cdf")
    Q3 = np.percentile(list, 75, method="averaged_inverted_cdf")

    dq = Q3 - Q1

    lower_limit = np.fmax(list[0], Q1 - 1.5*dq)
    upper_limit = np.fmin(list[-1], Q3 + 1.5*dq)

    diagram = plot.boxplot(list, labels=[label], positions=[pos])

# all municipalities

aux = []

for value in all_municipalities:
    aux.append(value["pop"])


# only southeast 

aux2 = []

for value in all_municipalities:
    if value["state"] == "SP" or value["state"] == "RJ" or value["state"] == "MG" or value["state"] == "ES":
         aux2.append(value["pop"])

boxplot(aux, "Brazil", 1)
boxplot(aux2, "Southeast", 2)

plot.title("Title")
plot.ylabel("Population")
plot.show()