import dash
from dash import html,dcc,callback
from dash.dependencies import Input, Output, State

dash.register_page(__name__)

globalUsername  = ''
globalType = ''

from pages.member.member import mainLayout as mainLayout
import pages.member.member as member

#layout for user log in
layout = html.Div(
     children=[
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
    [Output('page-content', 'children',allow_duplicate=True),
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
            global globalUsername, globalType
            globalUsername = username
            globalType = memberType
            #now to validate if it exits
            #need to create like a statement thing of whcih "welcome" it opens to  TO DO
            if (username == 'admin' and password == 'admin'):
                new_url = '/' + memberType + '/welcome'
                new_url = '/welcome'
                return mainLayout,dash.no_update,new_url
            
            #not validated
            else:
                print(memberType)
                return dash.no_update,"Incorrect. Please try again." ,'/login'


''' MEMBER VIEW'''
#functions for the buttons for MEMBER
            
#join class
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('joinClassButton', 'n_clicks'),
    prevent_initial_call=True
)
def join_class(n_clicks):
    if n_clicks:
        return 'Joined class!'


#Update Called
    #first function to generate the textfields
@callback(
     Output('buttonsTable','children',allow_duplicate=True),
     Input('updateInfoButton','n_clicks'),
     prevent_initial_call = True
)

def update_information(n_clicks):
    if n_clicks:
        print(globalUsername) #would have to change by getting the username value being used

        values = [('johnAdams@gmail.com','John',20,'male',150,50,60,'something')]

        return member.generateLayout(values)
    else:
        return dash.no_update
    
# second function for when the updaye is called
@callback(
    Output('confirmUpdate','displayed'),
    Output('page-content', 'children',allow_duplicate=True),
    Input('updateButton','n_clicks'),
    prevent_initial_call = True
)

def update_information_done(n_clicks):
    if n_clicks:
        #will have to call the function that updates the values //SQL
        return True,mainLayout 
    else:
        return False,dash.no_update    
