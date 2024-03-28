import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

from signUp import layout as signUpLayout
from logIn import layout as logInLayout
from welcome import layout as welcomeLayout

app = dash.Dash(__name__,suppress_callback_exceptions=True)


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
    [Output('page-content', 'children',allow_duplicate=True),
     Output('url', 'pathname')],
    [Input('signUpButton', 'n_clicks'),
     Input('logInButton', 'n_clicks')],
    [State('url', 'pathname')],
    prevent_initial_call=True
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


#dealing with log In page.
@app.callback(
    [Output('page-content', 'children',allow_duplicate=True),
    Output('failed','children')],
    [Input('logInSubmitButton','n_clicks')],
    [State('usernameInput','value'),
     State('passwordInput','value'),
     State('memberType','value'),
     State('url','pathname')],
    prevent_initial_call = True,
    
)

def validateUser(n_clicks,username,password,memberType,pathname):
    #if we're in the login page
    if pathname == '/login':
        if n_clicks:
            
            #now to validate if it exits
            if (username == 'admin' and password == 'admin'):
                print(memberType)
                return welcomeLayout,dash.no_update
            
            #not validated
            else:
                print(memberType)
                return dash.no_update, "FAILED"
    else:
        print("nothing has happened")
        return dash.no_update,dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)

