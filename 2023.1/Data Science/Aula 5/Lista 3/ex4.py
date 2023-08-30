import matplotlib.pyplot as plot
import numpy as np

data = {
    'salary': [13876, 11608, 18701, 11283, 11767, 20872, 11772, 10535, 12195, 12313, 14975, 21371, 19800, 11417, 20263, 13231, 12884, 13245, 15965, 12336, 21352, 13839, 16978, 14803, 
               22184, 13548, 14467, 15942, 23174, 23780],
    'experience': [1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,6,6,6,7,8,8,8,10,10,10,10],
    'education': ['Bacharel', 'Doutorado', 'Doutorado', 'Mestrado', 'Doutorado', 'Mestrado', 'Mestrado', 'Bacharel', 'Doutorado', 'Mestrado', 'Bacharel', 'Mestrado', 'Doutorado', 'Bacharel', 
                  'Doutorado', 'Doutorado', 'Mestrado', 'Mestrado', 'Bacharel', 'Bacharel', 'Doutorado', 'Mestrado', 'Bacharel', 'Mestrado', 'Doutorado', 'Bacharel', 'Bacharel', 'Mestrado', 
                  'Doutorado', 'Mestrado'],
    'management': ['Sim', 'Não', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Sim',
                    'Não', 'Não', 'Não', 'Sim', 'Sim']
}

listBacharel, listDoutorado, listMestrado = [], [], []
listBacharelS, listBacharelN, listDoutoradoS, listDoutoradoN, listMestradoS, listMestradoN = [], [], [], [], [], []

def organizeLists():
    for x in range(len(data['salary'])):

        if data['education'][x] == 'Bacharel':
            listBacharel.append(data['salary'][x])
            if data['management'][x] == 'Sim':
                listBacharelS.append(data['salary'][x])
            else:
                listBacharelN.append(data['salary'][x])

        elif data['education'][x] == 'Doutorado':
            listDoutorado.append(data['salary'][x])
            if data['management'][x] == 'Sim':
                listDoutoradoS.append(data['salary'][x])
            else:
                listDoutoradoN.append(data['salary'][x])
        
        else:
            listMestrado.append(data['salary'][x])
            if data['management'][x] == 'Sim':
                listMestradoS.append(data['salary'][x])
            else:
                listMestradoN.append(data['salary'][x])

def boxplot(list, label, pos):

    list.sort()

    Q1 = np.percentile(list, 25, method="averaged_inverted_cdf")
    Q2 = np.percentile(list, 50, method="averaged_inverted_cdf")
    Q3 = np.percentile(list, 75, method="averaged_inverted_cdf")

    dq = Q3 - Q1

    lower_limit = np.fmax(list[0], Q1 - 1.5*dq)
    upper_limit = np.fmin(list[-1], Q3 + 1.5*dq)

    diagram = plot.boxplot(list, labels=[label], positions=[pos])

organizeLists()

plot.figure(figsize=(18,8))

boxplot(listBacharel, 'All Bacharel', 1)
boxplot(listBacharelS, 'All Bacharel Sim', 2)
boxplot(listBacharelN, 'All Bacharel Não', 3)

boxplot(listDoutorado, 'All Doutorado', 4)
boxplot(listDoutoradoS, 'All Doutorado Sim', 5)
boxplot(listDoutoradoN, 'All Doutorado Não', 6)

boxplot(listMestrado, 'All Mestrado', 7)
boxplot(listMestradoS, 'All Mestrado Sim', 8)
boxplot(listMestradoN, 'All Mestrado Não', 9)

plot.title("Employees Salary")
plot.ylabel("Salary")
plot.show()