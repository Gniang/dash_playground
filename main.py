from os import path
import os
import dash
from dash.development.base_component import Component
import dash_core_components as dcc
from dash_core_components.Graph import Graph
from dash_core_components.Slider import Slider
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

ddir = r"cats"

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id='img_val', type='text'),
        html.Div(id='last_img'),

        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None,
        ),
    ],

    style={}
)


@app.callback(
    Output(component_id='last_img', component_property='children'),
    Input(component_id='img_val', component_property='value'),
)
def update_img(input_value: str):
    if input_value == None or not input_value.isdigit():
        return ""

    fname = '{:04}.jpg'.format(int(input_value))
    fpath = '{}/{}'.format(ddir, fname)
    return html.Img(
        id='img_{}'.format(fname),
        src=app.get_asset_url(fpath)
        # src=app.get_asset_url('cats/0001.jpg')
    )


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value')
)
def update_figure(selected_year):
    filterd_df = df[df.year == selected_year]
    fig = px.scatter(
        filterd_df,
        x="gdpPercap", y="lifeExp",
        size="pop", color="continent", hover_name="country",
        log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
