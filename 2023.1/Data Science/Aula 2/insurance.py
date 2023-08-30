import numpy as np
import matplotlib.pyplot as plot

values = [0.9, 1.0, 1.7, 2.9, 3.1, 5.3, 5.5, 6.9, 12.2, 12.9, 14.0, 33.6]

Q1 = np.percentile(values, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(values, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(values, 75, method="averaged_inverted_cdf")

dq = Q3 - Q1

lower_limit = np.fmax(values[0], Q1 - 1.5*dq)
upper_limit = np.fmin(values[len(values) - 1], Q3 + 1.5*dq)

diagram = plot.boxplot(values)

plot.title("Boxplot of Insurances")
plot.xlabel("Insurances")
plot.ylabel("Insurance Market Share")
plot.show()