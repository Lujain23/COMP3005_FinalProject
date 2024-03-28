import dash
from dash import html,dcc
from dash.dependencies import Input, Output, State


#this page is to log in the user depending on who it is
layout = html.Div([
    html.H1("Log In Page"),
    dcc.Input(id='usernameInput', type='text', placeholder='Enter username'),
    html.Br(),
    dcc.Input(id='passwordInput', type='password', placeholder='Enter password'),
    html.Br(),
    dcc.Dropdown(
        id='memberType',
        options=[
            {'label': 'Member', 'value': 'member'},
            {'label': 'Trainer', 'value': 'trainer'},
            {'label': 'Staff', 'value': 'staff'}
        ],

    ),
    html.Button('Submit', id='logInSubmitButton'),
    html.Div(id="failed")
])


