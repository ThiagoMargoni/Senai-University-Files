import matplotlib.pyplot as plot
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]

ya = []
yb = []
yc = []
tamanho = len(x)
contador = range(tamanho)

for i in contador:
    valor =  x[i] * x[i]        
    ya.append(valor)

    valor2 = x[i] * x[i]
    yb.append(valor2)

    valor3 = x[i] * x[i]
    yc.append(valor3)

matriz_corr = [x,ya,yb,yc]
rho = np.corrcoef(matriz_corr)

x_log = []
ya_log = []
yb_log = []
yc_log = []

for i in contador: 
    x_log.append(np.log(x[i]))
    ya_log.append(np.log(ya[i]))
    yb_log.append(np.log(yb[i]))
    yc_log.append(np.log(yc[i]))

matriz_corr_log = [x_log,ya_log,yb_log,yc_log]
rho_log = np.corrcoef(matriz_corr_log)

print(rho)
print(rho_log)

# graf_a = plot.scatter(x, ya)
# plot.show()
# graf_b = plot.scatter(x, yb)
# plot.show()
# graf_c = plot.scatter(x, yc)
# plot.show()

graf_a_log = plot.scatter(x_log, ya_log)
plot.show()
graf_b_log = plot.scatter(x_log, yb_log)
plot.show()
graf_c_log = plot.scatter(x_log, yc_log)
plot.show()