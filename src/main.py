from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from src.routing import RouteUrls
from src.server import app, LOCAL_STORAGE_ID  # define application server
from src.component import siderbar
from src.component import observe_content
from src.component import cameras_content
from src import theme

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# application main layout
app.layout = html.Div(
    [
        # url routing
        dcc.Location(id='url'),
        dcc.Store(id=LOCAL_STORAGE_ID, storage_type='local'),

        # メニュー
        siderbar.render(style=SIDEBAR_STYLE),

        # ヘッダー作りたい
        theme.dropdown,

        # メイン画面
        html.Div(id="main-content", style=CONTENT_STYLE),

        # テーマ変更機能の差し込み
        theme.switcher_component,
    ],

    style={}
)


@app.callback(Output("main-content", "children"), [Input("url", "pathname")])
def routeing_url(pathname: str):
    if pathname == RouteUrls.home:
        return observe_content.render()
    elif pathname == RouteUrls.camera_sts:
        return cameras_content.render()


if __name__ == '__main__':
    app.assets_ignore = 'bootstrap/*|bootswatch/*'
    app.config.suppress_callback_exceptions = True

    app.run_server(
        port='8050',
        debug=True,
        # dev_tools_hot_reload=False
    )
