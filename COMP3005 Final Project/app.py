import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

# import logIn


app = dash.Dash(__name__,suppress_callback_exceptions=True,use_pages=True)



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
        id='page-content', 
        children=[
    ]),
    dash.page_container
])


@app.callback(
    [ 
     Output('url', 'pathname',allow_duplicate=True)],
    [Input('signUpButton', 'n_clicks'),
     Input('logInButton', 'n_clicks')],
    [State('url', 'pathname')],
    prevent_initial_call=True
)
def switch_layout(signUp_clicks, logIn_clicks, current_path):
    print(current_path)
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if not ctx.triggered:
        return current_path

    if triggered_id == 'signUpButton' and signUp_clicks:
        return ['/signup']
    elif triggered_id == 'logInButton' and logIn_clicks:
        return ['/login']
    else:
        return current_path

if __name__ == '__main__':
    app.run_server(debug=True)

