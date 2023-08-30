import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

idade = np.array([1,2,3,4,5,6,7])
C = np.array([5.6,5.2,4.8,4.5,4.4,2.9,2.7])

print(idade.std())
print(np.std(C))

df_ex = pd.DataFrame({ "idade":idade, "conversão alimentar": C })
print(df_ex.head())

df_corr = df_ex.corr()

print(df_corr)

plt.plot(df_ex['idade'], df_ex['conversão alimentar'])
plt.show()