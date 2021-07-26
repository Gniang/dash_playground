from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.exceptions import PreventUpdate

from src.server import app, LOCAL_STORAGE_ID

CURRENT_SELECT_THEME = 'current_selected_theme'
DEFAULT_THEME = 'BOOTSTRAP'

themes_list = [
    "BOOTSTRAP",
    "CYBORG",
    "DARKLY",
    "SLATE",
    "SOLAR",
    "SUPERHERO",
    "CERULEAN",
    "COSMO",
    "FLATLY",
    "JOURNAL",
    "LITERA",
    "LUMEN",
    "LUX",
    "MATERIA",
    "MINTY",
    "PULSE",
    "SANDSTONE",
    "SIMPLEX",
    "SKETCHY",
    "SPACELAB",
    "UNITED",
    "YETI",
]

dropdown = dcc.Dropdown(
    id='theme_switcher',
    options=[{"label": str(i), "value": i} for i in themes_list],
    value=DEFAULT_THEME,
    clearable=False,
)

#
switcher_component = html.Div(id='theme_switcher_output')


@app.callback(
    Output('theme_switcher', 'value'),
    [
        Input(LOCAL_STORAGE_ID, 'modified_timestamp'),
    ],
    State(LOCAL_STORAGE_ID, 'data')
)
def on_current_select_theme(timestamp, current_seslect_theme) -> str:
    """前回選択されたテーマを再現する

    Returns:
        str: テーマ名
    """
    if timestamp is None:
        raise PreventUpdate

    if current_seslect_theme in themes_list:
        return current_seslect_theme

    return DEFAULT_THEME


# テーマ変更処理の差し込み
app.clientside_callback(
    """
    function(theme) {
        var stylesheet = document.querySelector('link[rel=stylesheet][href^="assets/boots"]')
        var name = theme.toLowerCase()
        if (name === 'bootstrap') {
            var link = 'assets/bootstrap/dist/css/bootstrap.min.css'
          } else {
            var link = "assets/bootswatch/dist/" + name + "/bootstrap.min.css"
        }
        stylesheet.href = link
    }
    """,
    Output("theme-switcher-output", "children"),
    Input("theme-switcher", "value"),
)
