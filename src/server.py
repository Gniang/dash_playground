import dash
import dash_bootstrap_components as dbc

LOCAL_STORAGE_ID = 'my_app_localstrage'

app = dash.Dash(__name__, external_stylesheets=[
                dbc.themes.BOOTSTRAP, "/assets/default.css"])
application = app.server
