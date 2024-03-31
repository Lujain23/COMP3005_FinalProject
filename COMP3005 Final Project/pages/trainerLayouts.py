from dash import  html,dcc
'''
setAvailiability() -> update availability of CURRENT trainer
getMember() -> select specific member (they have the name in their heads)
'''
rowStyle = {'fontSize':'20px','textAlign': 'center', 'width':'200px','height':'100px'}
#layout for the main buttons
mainLayout = html.Div(
    id = 'welcomeLayout',
    children=[
    
    html.Div(
        id = 'buttonsTable',
        children=[
        html.H1('Hello Trainer!'),
        html.H1('Welcome to the Health and Fitness Club!'),
        html.Table([
            html.Tr([
                html.Td(html.Button('Update Availability', id='updateAvailabilityButton', n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Search Member',id='getMemberButton',n_clicks=0, style=rowStyle))
            ]),       
        ], style = {'margin':'auto'}
        ) #end of table
    ])#end of div
])

columnStyle = {'fontSize':'20px','padding': '15px'}
getMemberLayout = html.Div([
        html.Div(
            id='initialLayout',
            children=[
                html.Label('Enter Member Name:', style={'fontSize': '20px', 'marginRight': '10px'}),
                dcc.Input(id='nameInput', type='text', style={'width': '300px', 'height': '30px', 'marginRight': '10px'}),
                html.Button('Submit Search', id='submitGetMemberButton', n_clicks=0, style={'width': '150px', 'fontSize': '16px', 'padding': '10px 20px'}),
            ],
            style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'center', 'alignItems': 'center', 'marginBottom': '20px'}
        ),  # End of first div

        html.Div(
            id='tableContainer',
            children=[
                html.Label('Member Information:', style={'fontSize': '30px'}),
                html.Table([
                    html.Thead(html.Tr([
                        html.Th('First Name', style=columnStyle),  
                        html.Th('Age', style=columnStyle),
                        html.Th('Gender', style=columnStyle),
                        html.Th('Height', style=columnStyle),
                        html.Th('Weight', style=columnStyle),
                        html.Th('Target Weight', style=columnStyle),
                        html.Th('Exercise Routine', style=columnStyle)
                    ])),
                    html.Tbody(id='memberTableBody'),
                    ],

                    style={'margin': 'auto', 'border': '2px solid #ddd', 'textAlign': 'center', 'width': '100%'}  
                ),
            ],
            style={'textAlign': 'center'}  
    )  # End of second div
])

