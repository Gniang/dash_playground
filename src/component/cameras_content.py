import dash_html_components as html
import dash_bootstrap_components as dbc


def render() -> html.Div:
    # not implemented
    return html.Div([
        dbc.Checklist(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
            ],
            value=[],
            id="switches-inline-input",
            inline=True,
            switch=True,
        ),
    ])
