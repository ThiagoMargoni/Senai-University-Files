

import plotly.subplots as sp
import plotly.graph_objects as go
import pandas as pd

# Dados de vendas
vendas = [5, 10, 14, 20, 25, 30, 35, 50, 100, 40, 150]
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro']

# Mapear os nomes dos meses para números de mês
meses_numeros = {'Janeiro': 1, 'Fevereiro': 2, 'Março': 3, 'Abril': 4, 'Maio': 5, 'Junho': 6, 'Julho': 7, 'Agosto': 8, 'Setembro': 9, 'Outubro': 10, 'Novembro': 11}

# Criar dataframe para os dados
df = pd.DataFrame({'Mês': meses, 'Vendas': vendas})
# Criar subplots
fig = sp.make_subplots(rows=2, cols=2,
                       subplot_titles=('Vendas Mensais', ' Vendas Mensais'),
                       specs=[[{'type': 'bar'}, {'type': 'indicator'}],
                              [{'type': 'table', 'colspan': 2}, None]])

# Gráfico de barras
fig.add_trace(go.Bar(x=df['Mês'], y=df['Vendas']), row=1, col=1)
fig.update_xaxes(title_text='Mês', row=1, col=1)
fig.update_yaxes(title_text='Vendas', row=1, col=1)
# Gráfico de gauge
fig.add_trace(go.Indicator(
    mode='gauge',
    value=df['Vendas'][10],
    domain={'x': [0, 0.4], 'y': [0.4, 0.5]},
    title={'text': ""},
    gauge={'axis': {'range': [None, max(vendas)]},
           'bar': {'color': 'darkblue'},
           'steps': [
               {'range': [0, 50], 'color': 'lightgray'},
               {'range': [50, 100], 'color': 'gray'}],
           'threshold': {'line': {'color': 'red', 'width': 4}, 'thickness': 0.75, 'value': max(vendas)}}), row=1, col=2)
# Tabela de vendas mensais
df_table = df.copy()
df_table['Mês'] = df_table['Mês'].map(meses_numeros)
df_table = df_table.sort_values('Mês')
df_table = df_table.reset_index(drop=True)
fig.add_trace(go.Table(
    header=dict(values=['Mês', 'Vendas'],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_table['Mês'], df_table['Vendas']],
               fill_color='lavender',
               align='left')), row=2, col=1)

fig.update_layout(height=800, width=800, showlegend=False,
                  plot_bgcolor='white',
                  paper_bgcolor='white',
                  font=dict(color='black'))
fig.write_html('Dashteste1')
fig.show()
