import matplotlib.pyplot as plot
import numpy as np

listH = [53,70.2,84.3,69.5,77.8,87.5,53.4,82.5,67.3,54.1,70.5,71.4,95.4,51.1,74.4,55.7,63.5,85.8,53.5,64.3,82.7,78.5,55.7,69.1,72.3,59.5,55.3,73,52.4,50.7]
listO = []

def boxplot(list, label, pos):

    list.sort()

    Q1 = np.percentile(list, 25, method="averaged_inverted_cdf")
    Q2 = np.percentile(list, 50, method="averaged_inverted_cdf")
    Q3 = np.percentile(list, 75, method="averaged_inverted_cdf")

    dq = Q3 - Q1

    lower_limit = np.fmax(list[0], Q1 - 1.5*dq)
    upper_limit = np.fmin(list[-1], Q3 + 1.5*dq)

    diagram = plot.boxplot(list, labels=[label], positions=[pos])

    string = ''
    for i in list:
        if i > upper_limit or i < lower_limit:
            string += f'\n -> {i};'

        if pos == 1:
            if i > (2.5*dq):
                listO.append(i)

    print(f'\nOutliers {label}: {string}' if string != '' else f'\n0 Outliers in {label}')

    if pos == 1:
        q95 = np.percentile(list, 95, method="averaged_inverted_cdf")
        q10 = np.percentile(list, 10, method="averaged_inverted_cdf")
        q90 = np.percentile(list, 90, method="averaged_inverted_cdf")

        string95 = f'Minor {q95}: '
        string80 = f'\nBetween {q10} ~ {q90}: '
        for x in list:
            if x <= q95:
                string95+=f'{x} - '

            if x <= q90 and x >= q10:
                string80+=f'{x} - '

        print(string95, string80)


boxplot(listH, "All Pieces", 1)
boxplot(listO, "New Outliers", 2)

plot.title("Hardness of Pieces")
plot.ylabel("Hardness")
plot.show()