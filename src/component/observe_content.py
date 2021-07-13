from dash.dependencies import Output,Input
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from src.server import app

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

datadir = r"cats"

def render() ->  html.Div:
    """監視画面　最新のカメラ画像一覧を表示する（定期的に更新する）

    Returns:
        html.Div: [description]
    """
    return html.Div([
        # 定期画面アプデ
        dcc.Interval(
            id='interval-component',
            interval=3*1000, # in milliseconds
            n_intervals=0
        ),
        

        html.Div(
            [
                html.Label('interval'),
                dcc.Input(id='interval_sec', type='text', value='3'),
            ]
        ),

        html.Div([
            html.Label('Image No'), 
            html.Label(id='img_val'),
        ]),

        html.Div([
            html.Img(id='last_img', style={'object-fit':'contain'}),
            ],
            style={'width':'300px', 'height':'400px'}
        ),

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
    
    style=CONTENT_STYLE)


# @app.callback(
#     Output(component_id='last_img', component_property='children'),
#     Input(component_id='img_val', component_property='value'),
# )
def create_img_path(input_value: str):
    if input_value == None or not input_value.isdigit():
        return ""

    fname = '{:03}.jpg'.format(int(input_value))
    fpath = '{}/{}'.format(datadir, fname)
    return app.get_asset_url(fpath)

class static:
    cnt = 0

@app.callback(Output('last_img', 'src'),
              Input('img_val', 'children'))
def update_metrics(img_val):
    return create_img_path(img_val)

@app.callback(Output('img_val', 'children'),
            Input('interval-component', 'n_intervals'),              
            )  
def update_text(n):
    static.cnt+=1
    return str(static.cnt)

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value')
)
def update_figure(selected_year):
    filterd_df = df[df.year == selected_year]
    fig = px.scatter(
        filterd_df,
        x="gdpPercap", y="lifeExp",
        labels={'gdpPercap':"x", 'lifeExp':"y"},
        # size="pos",
        color="continent", hover_name="country",
        log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig