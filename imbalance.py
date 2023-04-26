import requests
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Define the layout of the Dash app
app = dash.Dash()
color = 'grey'
# Function to update the graph with new data
counter = 0
max_points = 500
counter_list = []
new_imbalance_list = []

# Define the layout of the Dash app
app.layout = html.Div([
    dcc.Graph(id='live-graph', animate=True, style={'height': '1000px'}),
    dcc.Interval(id='graph-update', interval=2500, n_intervals=0)
])

# Update the graph with new data
@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph(n):
    global counter, color, counter_list, new_imbalance_list
    trades = requests.get('https://fapi.binance.com/fapi/v1/trades?symbol=ETHBUSD&limit=500').json()
    # Extract the timestamp, price and qty values from the trade data
    buys = [float(trade["price"])*(float(trade["qty"])) for trade in trades if trade["isBuyerMaker"]]
    sells = [float(trade["price"])*(float(trade["qty"])) for trade in trades if not trade["isBuyerMaker"]]
    counter += 1
    counter_list.append(counter)

    k = sum(buys)
    j = sum(sells)
    new_imbalance = (k - j) / (k + j)
    new_imbalance_list.append(new_imbalance)

    if counter > max_points:
        counter_list.clear()
        new_imbalance_list.clear()
        counter = 0

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=counter_list, y=new_imbalance_list[-500:], mode='lines', line=dict(color=color,width=10)))
    fig.update_xaxes(range=[counter-30, counter+5], autorange=True)
    fig.update_yaxes(range=[-1, 1], autorange=False)
    fig.update_layout(title='TRADE IMBALANCE',    shapes=[

        dict(
            type='line',
            x0=0,
            y0=0,
            x1=counter+5,
            y1=0,
            xref='x',
            yref='y',
            line=dict(
                color='black',
                width=3,
                dash='dot'
            ),
        )
    ])

    return fig

if __name__ == '__main__':
    app.run_server(debug=True,port=8050)
