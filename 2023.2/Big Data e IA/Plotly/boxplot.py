import plotly.graph_objects as go
import numpy as np

x_data = ['Carmelo Anthony', 'Dwyene Wade',"Deron Williams", 'Brook Lopez', 'Damian Wayne', 'David West']

N = 50
y0 =(10*np.random.randn(N)+30).astype(np.int64)
y1 =(13*np.random.randn(N)+38).astype(np.int64)
y2 =(11*np.random.randn(N)+33).astype(np.int64)
y3 =(9*np.random.randn(N)+36).astype(np.int64)
y4 =(15*np.random.randn(N)+31).astype(np.int64)
y5 =(12*np.random.randn(N)+40).astype(np.int64)

y_data=[y0,y1,y2,y3,y4,y5]
colors = ['rgba(93,164,214,0.5)','rgba(255,144,14,0.5)','rgba(44,160,101,0.5)','rgba(255,85,54,0.5)','rgba(207,114,255,0.5)''rgba(127,96,0,0.5)']

fig = go.Figure()
for xd,yd,cls in zip(x_data,y_data, colors):
    fig.add_trace(go.Box(
        y=yd,
        name=xd,
        boxpoints='all',
            jitter=0.5,
                whiskerwidth=0.2,
                    fillcolor=cls,
                        marker_size=2,
                            line_width=1)
                            )
    fig.show()