from dash import  html,dcc


rowStyle = {'fontSize':'20px','textAlign': 'center', 'width':'200px','height':'100px'}
dataStyle = {'fontSize':'18px', 'color': 'blue'}
boxStyle = {
    'width': '30%',
    'padding': '20px',
    'border': '2px solid #52489C',
    'border-radius': '10px',
    'margin': '10px',
    'box-shadow': '0px 0px 10px 0px rgba(0,0,0,0.1)',
}
textFieldStyle ={'width': '100%', 'height': '30px'}
textFieldStyle2 = {'width': '70%', 'height': '30px'}
columnStyle = {'fontSize':'20px','padding': '15px'}

#layout for the main buttons
def mainLayout(name):
    mainLayout = html.Div(
        id = 'welcomeLayout',
        children=[
        
        html.Div(
            id = 'buttonsTable',
            children=[
            html.H1([
                html.Span('Hello Member ',style={'color':'black'}),
                html.Span(name,style={'color':'#52489C'}),
                html.Span('!',style={'color':'black'}),
            ]),#heading done
            html.H1('Welcome to the Health and Fitness Club!'),
            html.Table([
                html.Tr([
                    html.Td(html.Button('Update Personal Information', id='updateInfoButton', n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('Join Class',id='joinClassButton',n_clicks=0, style=rowStyle))
                ]),
                html.Tr([
                    html.Td(html.Button('Print Dashboard',id='printDashboardButton',n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('Reschedule Class',id='rescheduleClassButton',n_clicks=0, style=rowStyle)),

                ]),  
                html.Tr([
                    html.Td(html.Button('Cancel Class',id='cancelClassButton',n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('View My Payments',id='viewPaymentButton',n_clicks=0, style=rowStyle))
                ]),
                html.Tr([
                    html.Td( html.Button('Go Back', id='typeMemberReturnButton', n_clicks=0, style = rowStyle),colSpan=2,style={'textAlign': 'center'})
                ]),                           
            ], style = {'margin':'auto'}
            ) #end of table
        ])#end of div
    ])
    return mainLayout

#layout for "join class"
def joinClassLayout(data):
    tableRows =[]

    for currClass in data:
        schedule_id, room_used, trainer_email, day_class,start_time, end_time, session_type, class_type = currClass
        currRow = html.Tr([html.Td(schedule_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(trainer_email,style=dataStyle), 
                               html.Td(day_class,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle), 
                                 html.Td(session_type,style=dataStyle),
                                   html.Td(class_type,style=dataStyle)])
        tableRows.append(currRow)

    columnStyle = {'fontSize':'20px','padding': '15px'}
    joinClassLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('Available Classes: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Schedule ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Trainer Email', style=columnStyle),
                            html.Th('On Day', style=columnStyle),
                            html.Th('Start Time', style=columnStyle),
                            html.Th('End Time', style=columnStyle),
                            html.Th('Session type', style=columnStyle),
                            html.Th('Class Type', style=columnStyle)
                        ])),
                        html.Tbody(id='classTableBody',children=tableRows),
                        ],

                        style={'margin': 'auto', 'border': '2px solid #ddd', 'textAlign': 'center', 'width': '100%'}  
                    ),
                ],
                style={'textAlign': 'center'}  
        ),  #first div
        html.Div(
        id='classToJoinContainer',
        children=[
            html.Label("Enter Schedule ID (just ID)",style={'font-size': '16px','margin-right':'10px'}),
            dcc.Input(id='scheduleIdInput', type='number', style={'width': '100px', 'margin-right': '10px','padding': '10px 20px'}),
            html.Button('Submit', id='submitJoinButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'}),
            html.Button('Go Back', id='goBackButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'}),
        ],
        style={'textAlign': 'center', 'margin': '20px auto'} 
    ),
    dcc.ConfirmDialog(
    id='joinSuccessful',
    message='Join Class was successful. Will return back to main menu.',
    ),
        
    ])
    return joinClassLayout

#layout for cancel class
def cancelClassLayout(data):
    tableRows =[]

    for currClass in data:
        schedule_id, room_used, trainer_email, class_day,start_time, end_time, session_type, class_type = currClass
        currRow = html.Tr([html.Td(schedule_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(trainer_email,style=dataStyle),
                               html.Td(class_day,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle), 
                                 html.Td(session_type,style=dataStyle),
                                   html.Td(class_type,style=dataStyle)])
        tableRows.append(currRow)

    columnStyle = {'fontSize':'20px','padding': '15px'}
    joinClassLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label("Enrolled Classes: ", style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Schedule ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Trainer Email', style=columnStyle),
                            html.Th('On Day', style=columnStyle),
                            html.Th('Start Time', style=columnStyle),
                            html.Th('End Time', style=columnStyle),
                            html.Th('Session type', style=columnStyle),
                            html.Th('Class Type', style=columnStyle)
                        ])),
                        html.Tbody(id='classTableBody',children=tableRows),
                        ],

                        style={'margin': 'auto', 'border': '2px solid #ddd', 'textAlign': 'center', 'width': '100%'}  
                    ),
                ],
                style={'textAlign': 'center'}  
        ),  # End of second div
        html.Div(
        id='classToJoinContainer',
        children=[
            html.Label("Enter Schedule ID (just ID)",style={'font-size': '16px','margin-right':'10px'}),
            dcc.Input(id='scheduleIdInput', type='number', style={'width': '100px', 'margin-right': '10px','padding': '10px 20px'}),
            html.Button('Submit', id='submitCancelButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'}),
            html.Button('Go Back', id='goBackButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'}),
        ],
        style={'textAlign': 'center', 'margin': '20px auto'} 
    ),
    dcc.ConfirmDialog(
    id='cancelSuccessful',
    message='Cancel Class was successful. Will return back to main menu.',
    ),
        
    ])
    return joinClassLayout

#layout for printDashboard
def generatePrintDashboardLayout(exercise_routine, height, weight, target_weight, BMI, isOverweight, weightChange, achievement):
    if(isOverweight):
        overweightSentence = "You are overweight."
    else:
        overweightSentence = "You are not overweight."

    line1 = f'Height: {height}'
    line2 = f'Current Weight : {weight}'
    line3 = f'Target Weight: {target_weight}'
    line4 =f'BMI:  {BMI}'
    line5 = overweightSentence
    line6 =  f'You are {weightChange} kg away from your target weight.'

    printDashboardLayout = html.Div([
        html.Div([
            html.H2('Exercise Routine', style={'color': '#52489C', 'margin-bottom': '10px'}),
            html.P(exercise_routine, style={'font-size': '18px'}),
        ], style=boxStyle),

        html.Div([
            html.H2('Fitness Achievement', style={'color': '#52489C', 'margin-bottom': '10px'}),
            html.P(achievement, style={'font-size': '18px'}),
        ], style=boxStyle),

        html.Div([
            html.H2('Health Statistics', style={'color': '#52489C', 'margin-bottom': '10px'}),
            html.P(line1, style={'font-size': '18px'}),
            html.P(line2, style={'font-size': '18px'}),
            html.P(line3, style={'font-size': '18px'}),
            html.P(line4, style={'font-size': '18px'}),
            html.P(line5, style={'font-size': '18px'}),
            html.P(line6, style={'font-size': '18px'}),

        ], style=boxStyle),
        html.Div([
            html.Button('Go Back', id='goBackButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'}),

        ])
        
    ], style={'display': 'flex', 'justify-content': 'space-between'},
    )
        
    return printDashboardLayout

#layout for updateMemberInfo
def generateLayout(values):
    
    layout = html.Div(
    id='page-content',
    children=[
        dcc.Location(id = 'url',refresh=False),
        html.Div([
            html.H1("Update Personal Information"),
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
                    html.Td(html.Label("Height (rounded to the nearest cm)")),
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
                ]),
                html.Tr([
                    html.Td(),
                    html.Td(html.Button('Go Back', id='goBackButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'}))
                ])
                                
            ], style={'margin-bottom': '10px', 'width': '100%'})
        ], style={'width': '100%'}),
        dcc.ConfirmDialog(
        id='confirmUpdate',
        message='Update Successful! Will go back to Main Menu.',
        ),
    ]
)
    return  layout

#layout for resechdule class - gotta make sure data only has the solo classes
def generateRescheduleClassLayout(data):
    tableRows =[]

    for currClass in data:
        schedule_id, room_used, trainer_email,day, start_time, end_time, session_type, class_type = currClass
        currRow = html.Tr([html.Td(schedule_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(trainer_email,style=dataStyle), 
                               html.Td(day,style=dataStyle),
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle), 
                                 html.Td(session_type,style=dataStyle),
                                   html.Td(class_type,style=dataStyle)])
        tableRows.append(currRow)

    columnStyle = {'fontSize':'20px','padding': '15px'}
    rescheduleClassLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('Solo Classes to Reschedule: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Schedule ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Trainer Email', style=columnStyle),
                            html.Th('On Day', style=columnStyle),
                            html.Th('Start Time', style=columnStyle),
                            html.Th('End Time', style=columnStyle),
                            html.Th('Session type', style=columnStyle),
                            html.Th('Class Type', style=columnStyle)
                        ])),
                        html.Tbody(id='classTableBody',children=tableRows),
                        ],

                        style={'margin': 'auto', 'border': '2px solid #ddd', 'textAlign': 'center', 'width': '100%'}  
                    ),
                ],
                style={'textAlign': 'center'}  
            ),  #first div
            html.Br(),
            html.Br(),
            html.Div(
                children = [

                    html.Table([
                            html.Tr([
                                html.Td(html.Label('Schedule ID:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='scheduleIdInput', type='text', placeholder='Enter schedule ID',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Start Time HH:MM::SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='startInput', type='text', placeholder='Enter start time',style=textFieldStyle2)),
                            ]),  
                            html.Tr([
                                html.Td(html.Label('End Time HH:MM:SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='endInput', type='text', placeholder='Enter end time ',style=textFieldStyle2))
                            ]), 
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Submit', id='submitRescheduleButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='goBackButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
            ), #second div
            html.Div(id='rescheduleOutcome'),
            dcc.ConfirmDialog(
            id='rescheduleSuccessful',
            message='Reschedule Class was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return rescheduleClassLayout

def generateDesignViewPayments(data):
    allReceiptsList = []

    receipStyle = {
        'font-family': 'Arial, sans-serif',
        'color': '#52489C',
        'border': '2px solid #52489C',
        'border-radius': '10px',
        'padding': '20px',
        'margin': '10px',
        'box-shadow': '0px 0px 10px 0px rgba(0,0,0,0.1)'
    }
    if(len(data) == 0):
        #there are no payments
        noPayments = html.Div(
            id = 'page-content',
            children=[
                html.H1('WOOHOO No payments!', style={'fontSize': '36px', 'textAlign': 'center', 'color': '#52489C'}),
                html.Button('Go Back', id='goBackButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})
            ]
        )
        return noPayments
    

    for currReceipt in data:
        payment_id,amount, transaction_date, status, description = currReceipt
        finalizedSingleReceipt = html.Div(
            children=[
                html.Br(),
                html.P(f"Payment ID: {payment_id}",style={'fontSize':'20px','fontWeight': 'bold'}),
                html.P(f"Amount: ${amount:.2f}"),
                html.P(f"Transaction Date: {transaction_date}"),
                html.P(f"Status: {status}"),
                html.P(f"Description: {description}")
            ],
            style=receipStyle
        )
        allReceiptsList.append(finalizedSingleReceipt)

    allReceipts = html.Div(
                    id ='page-content',
                    children=[
                        html.Br(),
                        html.Br(),
                        html.H1('My Payments',style={'fontSize':'24px','color': '#52489C'}),
                        html.Br(),
                        html.Div(allReceiptsList),
                        html.Div(
                            html.Table([
                                html.Tr([
                                    html.Td(html.Label('Enter Payment ID:',style={'fontSize':'20px'})),
                                    html.Td(dcc.Input(id='payReceiptInput', type='text',style=textFieldStyle)),
                                    html.Td(html.Button('Pay!', id='payReceiptButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px','marginRight':'10px'}))
                                ]),
                                html.Tr([
                                    html.Td(),
                                    html.Td(),
                                    html.Td(html.Button('Go Back', id='goBackButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                                ]),                                
                            ]),
                        ),#end of div,
                        html.Div(id='payReceiptOutcome'),
                        dcc.ConfirmDialog(
                        id='memberPaySuccessful',
                        message='Payment was successful. Will return back to main menu.',
                        ),                     
                    ]
    )
    
    return allReceipts