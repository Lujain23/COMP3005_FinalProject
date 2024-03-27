import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

from signUp import layout as signUpLayout
from logIn import layout as logInLayout

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[
        html.Div([
            html.Button('Sign Up', id='signUpButton', n_clicks=0, style={'fontSize': 20}),
            html.Br(),
            html.Br(),
            html.Button('Log In', id='logInButton', n_clicks=0, style={'fontSize': 20}),
        ], style={'textAlign': 'center', 'margin': 'auto', 'width': '50%'})
    ]),
])


@app.callback(
    [Output('page-content', 'children'),
     Output('url', 'pathname')],
    [Input('signUpButton', 'n_clicks'),
     Input('logInButton', 'n_clicks')],
    [State('url', 'pathname')]
)
def switch_layout(signUp_clicks, logIn_clicks, current_path):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if not ctx.triggered:
        return dash.no_update, current_path

    if triggered_id == 'signUpButton' and signUp_clicks:
        return signUpLayout, '/signup'
    elif triggered_id == 'logInButton' and logIn_clicks:
        return logInLayout, '/login'
    else:
        return dash.no_update, current_path

if __name__ == '__main__':
    app.run_server(debug=True)

