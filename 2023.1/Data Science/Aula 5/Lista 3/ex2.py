import matplotlib.pyplot as plot
import numpy as np

listB = [1,2,4,4,7,3,3,2,4,5,2,4,3,5,3,2,4,3,6,5,5,6,4,6,5]
listS = [1,7,7,6,1,2,6,1,7,2,1,3,2,7,5,6,1,7,4,1,5,7,6,3,2]

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

boxplot(listB, "Basketball ", 1)
boxplot(listS, "Soccer", 2)

plot.title("Lesions on Sports")
plot.ylabel("Number")
plot.show()