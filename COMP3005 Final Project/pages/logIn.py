import dash
from dash import html,dcc,callback
from dash.dependencies import Input, Output, State

dash.register_page(__name__)

from pages.member.welcome import layout as welcomeLayout

#layout for user log in
layout = html.Div(
     [
          dcc.Location(id='url',refresh=False),
          html.Div(
                style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'},
                id='page-content',
                children=[
                    html.Div([
                        html.H1("Log In Page"),
                        dcc.Input(id='usernameInput', type='text', placeholder='Enter username'),
                        html.Br(),
                        html.Br(),
                        dcc.Input(id='passwordInput', type='password', placeholder='Enter password'),
                        html.Br(),
                        html.Br(),
                        dcc.Dropdown(
                            id='memberType',
                            options=[
                                {'label': 'Member', 'value': 'member'},
                                {'label': 'Trainer', 'value': 'trainer'},
                                {'label': 'Staff', 'value': 'staff'}
                            ],

                        ),
                        html.Br(),
                        html.Br(),
                        html.Button('Submit', id='logInSubmitButton'),
                        html.Div(id="failed")
                    ])
                ]  
          )
     ]

)



#dealing with log In page.
@callback(
    [Output('page-content', 'children'),
    Output('failed','children'),
    Output('url','pathname',allow_duplicate=True)],
    [Input('logInSubmitButton','n_clicks')],
    [State('usernameInput','value'),
     State('passwordInput','value'),
     State('memberType','value')],
    prevent_initial_call = True,
    
)

def validateUser(n_clicks,username,password,memberType):
    #if we're in the login page
        if n_clicks:
            
            #now to validate if it exits
            if (username == 'admin' and password == 'admin'):
                new_url = '/' + memberType + '/welcome'
                return welcomeLayout,dash.no_update,new_url
            
            #not validated
            else:
                print(memberType)
                return dash.no_update,"Incorrect. Please try again." ,'/login'


