import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

layout = html.Div([
    html.H1('Sign Up Page'),
    html.Div([
        html.P('Sign up form goes here...')
    ])
])
