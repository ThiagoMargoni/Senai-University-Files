import numpy as np
import matplotlib.pyplot as plot

# All Municipalities

all_municipalities = [988.8, 556.9, 224.6, 210.9, 201.5, 187.7, 151.6, 135.8, 129.9, 119.4, 116.0, 102.3, 101.8, 92.4, 84.7, 
          83.9, 80.2, 74.7, 72.7, 68.4, 66.8, 66.8, 63.7, 62.8, 61.9, 56.2, 54.1, 50.3, 49.7, 46.3]

all_municipalities.sort()

Q1 = np.percentile(all_municipalities, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(all_municipalities, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(all_municipalities, 75, method="averaged_inverted_cdf")

dq = Q3 - Q1

lower_limit = np.fmax(all_municipalities[0], Q1 - 1.5*dq)
upper_limit = np.fmin(all_municipalities[len(all_municipalities) - 1], Q3 + 1.5*dq)

# Only Southeast Municipalities

only_southeast = [988.8, 556.9, 210.9, 101.8, 92.4, 84.7, 83.9, 72.7, 68.4, 63.7, 62.8, 50.3, 49.7, 46.3]

print(len(only_southeast))

only_southeast.sort()

Q1 = np.percentile(only_southeast, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(only_southeast, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(only_southeast, 75, method="averaged_inverted_cdf")

dq = Q3 - Q1

lower_limit = np.fmax(only_southeast[0], Q1 - 1.5*dq)
upper_limit = np.fmin(only_southeast[-1], Q3 + 1.5*dq)

# Results

diagram_g = plot.boxplot(all_municipalities, labels=["Brazil"], positions=[1])
diagram_s = plot.boxplot(only_southeast, labels=["Southeast"], positions=[2])

plot.title("Title")
plot.ylabel("Population")
plot.show()