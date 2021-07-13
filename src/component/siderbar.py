
from typing import Dict
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_bootstrap_components._components.Nav import Nav

from src.routing import RouteUrls

 

def render(style:Dict) -> Nav: 
    """ サイドバー表示
    """
    return html.Div([
        dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Home", href=RouteUrls.home)),
            dbc.NavItem(dbc.NavLink("Cameras", href=RouteUrls.camera_sts))
        ],
        vertical=True
        )
    ],
    style = style) 
