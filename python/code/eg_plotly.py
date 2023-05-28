# FILE: eg_plotly.py
from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

app = Dash()

md_text = '''
# Dash with Markdown

##  Header 2

Put some write up here.

- bullet *point 1*
- bullet **point 2**
'''

data = pd.read_csv('data/XAUUSD.csv', parse_dates=['Date'])
print(data)
fig = go.Figure(
    data=[
        go.Candlestick(x=data['Date'],
                       open=data['Open'],
                       high=data['High'],
                       low=data['Low'],
                       close=data['Close']
                       )
        ]
    )


app.layout = html.Div(
    [
     html.H1('Dashboard'),
     html.Div(dcc.Markdown(md_text)),
     html.Div(dcc.Graph(figure=fig))
     ])
app.run_server(debug=True)