import plotly.express as px #Importação do ploty
import numpy as np

# fig = px.bar(x=["a","b","c"], y =[1,2,3])
# fig.update_traces(marker_color = "darkcyan")
# fig.show()

t = np.linspace(0,2 * np.pi,100)
fig = px.line(x=t,y=np.cos(t),labels={'x':'t','y': 'cos(t)'})
fig.show()

t = np.linspace(0,2 * np.pi,100)
fig = px.line(x=t,y=np.sin(t),labels={'x':'t','y': 'sin(t)'})
fig.show()

t = np.linspace(0,2 * np.pi,100)
fig = px.line(x=t,y=np.tan(t),labels={'x':'t','y': 'tan(t)'})
fig.show()