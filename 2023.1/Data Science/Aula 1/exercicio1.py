# Ex. 1 - Lista 1

import numpy as np;
import statistics as st;

resis = [348.5, 340.1, 360.8, 353.2, 357.6];

media = np.mean(resis);
mediana = np.median(resis);
dp = np.std(resis);
moda = st.mode(resis);

print(media, mediana, dp, moda);
# arrendondar duas casas
print("A média é igual a: %.2f" %(media));
# resultados juntos
print("A média é igual a: %.ff \nA mediana é: %d \nO Desvio Padrão é igual a: %.2f \nA moda é igual a: %.1f" %(media, mediana, dp, moda));