from dash import  html,dcc


#this is the welcome page for the member

#should create buttons for these
'''
def updateMemberInformation():
def printDashboard(): -> sh
def joinClass():
def rescheduleClass():
def cancelClass():
'''


rowStyle = {'fontSize':'20px','textAlign': 'center', 'width':'200px','height':'100px'}
#layout for the main buttons
mainLayout = html.Div(
    id = 'welcomeLayout',
    children=[
    
    html.Div(
        id = 'buttonsTable',
        children=[
        html.H1('Hello Member!'),
        html.H1('Welcome to the Health and Fitness Club!'),
        html.Table([
            html.Tr([
                html.Td(html.Button('Update Personal Information', id='updateInfoButton', n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Join Class',id='joinClassButton',n_clicks=0, style=rowStyle))
            ]),
            html.Tr([
                html.Td(html.Button('Print Fitness and Routine',id='printExerciseButton',n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Reschedule Class',id='rescheduleClassButton',n_clicks=0, style=rowStyle)),

            ]),  
            html.Tr([
                html.Td(html.Button('Print Health Statistics',id='printHealthButton',n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Cancel Class',id='cancelClassButton',n_clicks=0, style=rowStyle))
            ]),             
        ], style = {'margin':'auto'}
        ) #end of table
    ])#end of div
])

#layout for "join class"


#layout for printDashboard

#layout for cancel class

#layout for updateMemberInfo
def generateLayout(values):
    textFieldStyle ={'width': '100%', 'height': '30px'}
    layout = html.Div(
    id='page-content',
    children=[
        dcc.Location(id = 'url',refresh=False),
        html.Div([
            html.H1("User Registration Form"),
            html.Table([
                html.Tr([
                    html.Td(html.Label("Email")),
                    html.Td(dcc.Input(id='emailInput', type='email', style=textFieldStyle,value=values[0][0],readOnly= True))
                ]),
                html.Tr([
                    html.Td(html.Label("Password")),
                    html.Td(dcc.Input(id='passwordInput', type='text', style=textFieldStyle,value=values[0][1]))
                ]),
                html.Tr([
                    html.Td(html.Label("First Name")),
                    html.Td(dcc.Input(id='nameInput', type='text', style=textFieldStyle,value=values[0][2]))
                ]),
                html.Tr([
                    html.Td(html.Label("Age")),
                    html.Td(dcc.Input(id='ageInput', type='number', style=textFieldStyle,value=values[0][3]))
                ]),
                html.Tr([
                    html.Td(html.Label("Gender")),
                    html.Td(dcc.Input(id='genderInput', type='text', style=textFieldStyle,value=values[0][4]))
                ]),
                html.Tr([
                    html.Td(html.Label("Height (rounded to the nearest m)")),
                    html.Td(dcc.Input(id='heightInput', type='number', style=textFieldStyle,value=values[0][5]))
                ]),
                html.Tr([
                    html.Td(html.Label("Weight (rounded to the nearest kg)")),
                    html.Td(dcc.Input(id='weightInput', type='number', style=textFieldStyle,value=values[0][6]))
                ]),
                html.Tr([
                    html.Td(html.Label("Target Weight (rounded to the nearest kg)")),
                    html.Td(dcc.Input(id='targetInput', type='number', style=textFieldStyle,value=values[0][7]))
                ]),
                html.Tr([
                    html.Td(html.Label("Exercise Routine")),
                    html.Td(dcc.Input(id='exerciseRoutineInput', type='text', style=textFieldStyle,value=values[0][8]))
                ]),
                html.Tr([
                    html.Td(),
                    html.Td(html.Button('Update Information', id='updateButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'}))
                ])
                                
            ], style={'margin-bottom': '10px', 'width': '100%'})
        ], style={'width': '50%'}),
        dcc.ConfirmDialog(
        id='confirmUpdate',
        message='Update Successful! Will go back to Main Menu.',
        ),
    ]
)
    return  layout


