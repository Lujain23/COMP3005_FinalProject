import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State

dash.register_page(__name__)

textFieldStyle ={'width': '100%', 'height': '30px'}

# #have to create divs for each texfield to be under each other

layout= html.Div(
    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'},
    id='page-content',
    children=[
        dcc.Location(id = 'url',refresh=False),
        html.Div([
            html.H1("User Registration Form"),
            html.Table([
                html.Tr([
                    html.Td(html.Label("Email")),
                    html.Td(dcc.Input(id='emailInput', type='email', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(html.Label("Password")),
                    html.Td(dcc.Input(id='passwordInput', type='text', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(html.Label("First Name")),
                    html.Td(dcc.Input(id='nameInput', type='text', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(html.Label("Age")),
                    html.Td(dcc.Input(id='ageInput', type='number', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(html.Label("Gender")),
                    html.Td(dcc.Input(id='genderInput', type='text', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(html.Label("Height (rounded to the nearest m)")),
                    html.Td(dcc.Input(id='heightInput', type='number', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(html.Label("Weight (rounded to the nearest kg)")),
                    html.Td(dcc.Input(id='weightInput', type='number', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(html.Label("Target Weight (rounded to the nearest kg)")),
                    html.Td(dcc.Input(id='targetInput', type='number', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(html.Label("Exercise Routine")),
                    html.Td(dcc.Input(id='exerciseRoutineInput', type='text', style=textFieldStyle))
                ]),
                html.Tr([
                    html.Td(),
                    html.Td(html.Button('Register', id='registerButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'}))
                ])
                                
            ], style={'margin-bottom': '10px', 'width': '100%'})
        ], style={'width': '50%'})
    ]
)

successLayout = html.Div([
    html.H1("Registeration Successful!"),
    html.H1("You will be redirected to the Main Menu and can log in."),
])

#when submit button is clicked
@callback(
   [Output('url','pathname'),
    Output('page-content','children',allow_duplicate=True)],
   [Input('registerButton','n_clicks')],
   [State('emailInput','value'),
    State('nameInput','value'),
    State('ageInput','value'),
    State('genderInput','value'),
    State('heightInput','value'),
    State('weightInput','value'),
    State('targetInput','value'),
    State('exerciseRoutineInput','value'),
    ],
    prevent_initial_call=True
)
def registerMember(n_clicks,email,firstName,age,gender,height,weight,target,exceriseRoutie):
    if n_clicks:
        if (email and firstName and age and gender and height and weight and target):
            return '/',successLayout
        else:
            return '/signup',dash.no_update
        
#after signing up successfully, to alert the user register successful and to sign in again