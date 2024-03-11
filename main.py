from dash import Dash, dcc, html 
import pandas as pd

## Creating and cleaning the dataframe
data = pd.read_csv('/home/marcus/Documents/Scripts/DashPlotly Example/avocado.csv')
data = data.query("type == 'conventional' and region == 'Albany'")
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data.sort_values('Date', inplace=True)

app = Dash(__name__) # Creating an instance of the Dash class

app.layout = html.Div(  # Dashboard layout and components html for text, dcc for graphs and such..
    children = [
        html.H1(children="Avocado Analytics",),
        html.P(
            children = "Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2014 and 2018",
        ),
        dcc.Graph(
            figure = {
                "data": [
                    {
                        'x': data['Date'],
                        'y': data['AveragePrice'],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': data['Date'],
                        'y': data["Total Volume"],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': "Avocados Sold"},
            },
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
