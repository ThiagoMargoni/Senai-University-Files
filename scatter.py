import plotly.graph_objects as go #Importação do ploty
import numpy as np

# t = np.linspace(0,10,100) # cria espaçamento igualmente dividos 100 vezes de 0 e 10
# y= np.sin(t)
# fig = go.Figure(data=go.Scatter(x=t, y=y, mode="markers"))
# fig.show()

np.random.seed(1)
N = 100
random_x = np.linspace(0,1,N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5
fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0, mode='markers', name = 'markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1, mode='lines+markers', name = 'lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2, mode='lines', name = 'lines'))
fig.write_html('grafico plotly.html')
fig.show()