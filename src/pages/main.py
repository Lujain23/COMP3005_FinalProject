import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

dash.register_page(__name__,path="/")
buttonStyle = {'font-weight': 'bold','fontSize':'25px','width':'50%','height':'100px', 'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center','marginLeft':'150px','marginTop':'100px','backgroundColor': '#a2d2ff'}
layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content', children=[
            html.Div([
            html.Button('Sign Up', id='signUpButton', n_clicks=0, style=buttonStyle),
            html.Br(),
            html.Br(),
            html.Button('Log In', id='logInButton', n_clicks=0, style=buttonStyle),
        ], style={'textAlign': 'center', 'margin': 'auto', 'width': '50%'})
    ]),
])
