import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.svm import SVR

mesh_size = .02
margin = 0
df = px.data.iris()
x = df[['sepal_width','sepal_length']]
y = df ['petal_width']
model = SVR(C=1.0)
model.fit(x,y)

x_min, x_max = x.sepal_width.min()- margin, x.sepal_length.max()+margin
y_min, y_max = x.sepal_width.min()- margin, x.sepal_length.max()+margin
xrange = np.arange(x_min,x_max,mesh_size)
yrange = np.arange(y_min,y_max,mesh_size)
xx,yy = np.meshgrid(xrange,yrange)

pred = model.predict(np.c_[xx.ravel(),yy.ravel()])
pred = pred.reshape(xx.shape)

fig = px.scatter_3d(df,x='sepal_width', y='sepal_length', z= 'petal_width')
fig.update_traces(marker=dict(size=5))
fig.add_trace(go.Surface(x=xrange,y=yrange,z=pred, name= 'pred_surface'))
fig.show()