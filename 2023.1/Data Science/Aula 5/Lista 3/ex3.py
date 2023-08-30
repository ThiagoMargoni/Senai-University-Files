import matplotlib.pyplot as plot
import numpy as np

listF = [154, 109, 137, 115, 152, 140, 154, 178, 101, 103, 126, 126, 137, 165, 165, 129, 200, 148]
listOutlierF = []
listM = [108, 140, 114, 91, 180, 115, 126, 92, 169, 146, 109, 132, 75, 88, 113, 151, 70, 115, 187, 104]
listClass = listF + listM

def boxplot(list, label, pos):

    list.sort()

    Q1 = np.percentile(list, 25, method="averaged_inverted_cdf")
    Q2 = np.percentile(list, 50, method="averaged_inverted_cdf")
    Q3 = np.percentile(list, 75, method="averaged_inverted_cdf")

    dq = Q3 - Q1

    lower_limit = np.fmax(list[0], Q1 - 1.5*dq)
    upper_limit = np.fmin(list[-1], Q3 + 1.5*dq)

    diagram = plot.boxplot(list, labels=[label], positions=[pos])

    print(f'\n-----------------{label}-----------------\nAverage: {np.average(list):.1f}\nMedian: {Q2:.1f}')
    
    if pos == 1:
        for i in list:
            if i < upper_limit and i > lower_limit:
                listOutlierF.append(i)


boxplot(listF, "Female", 1)
boxplot(listOutlierF, "Female Without Outlier", 2)
boxplot(listM, "Male", 3)
boxplot(listClass, "All Class", 4)

plot.title("Student's Grades")
plot.ylabel("Grades")
plot.show()