from dash import  html,dcc

rowStyle = {'fontSize':'20px','textAlign': 'center', 'width':'200px','height':'100px'}
dataStyle = {'fontSize':'18px', 'color': 'blue'}
textFieldStyle2 = {'width': '70%', 'height': '30px'}
columnStyle = {'fontSize':'20px','padding': '15px'}

#layout for the main buttons
mainLayout = html.Div(
    id = 'welcomeLayout',
    children=[
    
    html.Div(
        id = 'buttonsTable',
        children=[
        html.H1('Hello Staff!'),
        html.H1('Welcome to the Health and Fitness Club!'),
        html.Table([
            html.Tr([
                html.Td(html.Button('Add Class', id='addClassButton', n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Remove Class',id='removeClassButton',n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Modify Class', id='modifyClassButton', n_clicks=0, style=rowStyle))
            ]),  
            html.Tr([
                html.Td(html.Button('Print Maintenance',id='printMaintenanceButton',n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Add Equipment Check', id='addEquipmentButton', n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Update Maintenance Check',id='updateMaintenanceButton',n_clicks=0, style=rowStyle))
            ]),   
            html.Tr([
                html.Td(html.Button('Add Room Booking', id='addRoomBookingButton', n_clicks=0, style=rowStyle)),
                html.Td(html.Button('Print Used Rooms',id='printUsedRoomsButton',n_clicks=0, style=rowStyle)),
                html.Td(html.Button('History Of Payments', id='printReceiptButton', n_clicks=0, style=rowStyle))
            ]),  
                
        ], style = {'margin':'auto'}
        ) #end of table
    ])#end of div
])

def generateRemoveClassLayout(data):
    tableRows =[]

    for currClass in data:
        schedule_id, room_used, trainer_email, start_time, end_time, session_type, class_type = currClass
        currRow = html.Tr([html.Td(schedule_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(trainer_email,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle), 
                                 html.Td(session_type,style=dataStyle),
                                   html.Td(class_type,style=dataStyle)])
        tableRows.append(currRow)

    columnStyle = {'fontSize':'20px','padding': '15px'}
    removeClassLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('All Current Classes: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Schedule ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Trainer Email', style=columnStyle),
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
                                html.Td(dcc.Input(id='classToRemoveInput', type='text',style=textFieldStyle2))
                            ]),
    
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Submit', id='submitStaffRemoveClassButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
            ), #second div
            html.Div(id='staffRemoveClassOutcome'),
            dcc.ConfirmDialog(
            id='staffRemoveClassSuccessful',
            message='Removing Class was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return removeClassLayout    

def generateModifyClassLayout(data):
    tableRows =[]

    for currClass in data:
        schedule_id, room_used, trainer_email, start_time, end_time, session_type, class_type = currClass
        currRow = html.Tr([html.Td(schedule_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(trainer_email,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle), 
                                 html.Td(session_type,style=dataStyle),
                                   html.Td(class_type,style=dataStyle)])
        tableRows.append(currRow)

    columnStyle = {'fontSize':'20px','padding': '15px'}
    modifyClassLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('All Current Classes: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Schedule ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Trainer Email', style=columnStyle),
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
                                html.Td(dcc.Input(id='StaffscheduleIdInput', type='text', placeholder='Enter schedule ID',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Start Time HH:MM::SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='StaffstartInput', type='text', placeholder='Enter start time',style=textFieldStyle2)),
                            ]),  
                            html.Tr([
                                html.Td(html.Label('End Time HH:MM:SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='StaffendInput', type='text', placeholder='Enter end time ',style=textFieldStyle2))
                            ]), 
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Submit', id='submitModifyClassButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
            ), #second div
            html.Div(id='staffModifyClassOutcome'),
            dcc.ConfirmDialog(
            id='staffmodifyClassSuccessful',
            message='Modifying Class was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return modifyClassLayout  

def generateAddClassLayout(data):
    tableRows =[]

    for currClass in data:
        schedule_id, room_used, trainer_email, start_time, end_time, session_type, class_type = currClass
        currRow = html.Tr([html.Td(schedule_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(trainer_email,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle), 
                                 html.Td(session_type,style=dataStyle),
                                   html.Td(class_type,style=dataStyle)])
        tableRows.append(currRow)

    columnStyle = {'fontSize':'20px','padding': '15px'}
    addClassLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('All Current Classes: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Schedule ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Trainer Email', style=columnStyle),
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
                                html.Td(html.Label('Room to use:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='roomUsedInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Trainer Email:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='trainerInput', type='text',style=textFieldStyle2))
                            ]),                            
                            html.Tr([
                                html.Td(html.Label('Start Time HH:MM::SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='startInput', type='text',style=textFieldStyle2)),
                            ]),  
                            html.Tr([
                                html.Td(html.Label('End Time HH:MM:SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='endInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Session Type: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Dropdown(id='sessionTypeInput', options=[{'label' : 'Group','value' :'group'}, {'label' : 'Solo','value' :'solo'}], style={**textFieldStyle2,'marginBottom' : '10px'}))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Description of Session: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='description', type = 'text', style=textFieldStyle2))
                            ]),    
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Submit', id='submitStaffAddClassButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
            ), #second div
            html.Div(id='staffAddClassOutcome'),
            dcc.ConfirmDialog(
            id='staffAddClassSuccessful',
            message='Creating Class was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return addClassLayout

def generateUpdateEquipmentLayout():
    mainStyle = {'fontSize':'20px','marginRight':'10px'}
    layout = html.Div(
        id='page-content',
        children=[
            html.Div(
                children=[
                    html.H1("Updating the Equipment:",style={'fontSize':'28px','textAlign' :'center'})
                ]
            ), #first div
            html.Br(),
            html.Br(),
            html.Div(
                children=[
                    html.Label('Equipment that was checked:',style=mainStyle),
                    dcc.Input(id='equipmentNameInput', type='text',style=mainStyle),
                ]
            ), #second div
            html.Br(),
            html.Br(),
            html.Div(
                children=[
                    html.Button('Update', id='updateEquipmentButton', n_clicks=0, style={**mainStyle,'width':'35%','height':'40px'}),
                    html.Br(),
                    html.Br(),
                    html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={**mainStyle,'width':'35%','height':'40px'})                    
                ],
                style={'textAlign': 'center'}
            ), #third
            dcc.ConfirmDialog(
            id='staffUpdateEquipmentSuccessful',
            message='Updating Date of equipment check was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return layout 

def generateAddEquipmentLayout():
    mainStyle = {'fontSize':'20px','marginRight':'10px'}
    layout = html.Div(
        id='page-content',
        children=[
            html.Div(
                children=[
                    html.H1("Add New Equipment:",style={'fontSize':'28px','textAlign' :'center'})
                ]
            ), #first div
            html.Br(),
            html.Br(),
            html.Table([
                html.Tr([
                html.Td(html.Label('New Equipment To add:',style=mainStyle)),
                html.Td(dcc.Input(id='newEquipmentNameInput', type='text',style=mainStyle))
                ]),
                html.Tr([
                html.Td(html.Label('Equipment is in room:',style=mainStyle)),
                html.Td(dcc.Input(id='roomEquipmentInput', type='text',style=mainStyle)), 
                ]),
                html.Tr([
                    html.Td(),
                    html.Td( html.Button('Add Equipment', id='addEquipmentButton', n_clicks=0, style={**mainStyle,'width':'70%','height':'40px'})),                                 
                ]),                  
                html.Tr([
                    html.Td(),
                    html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0,  style={**mainStyle,'width':'70%','height':'40px'})),                                 
                ])  
            ]),            

            dcc.ConfirmDialog(
            id='staffaddEquipmentSuccessful',
            message='Addinge of equipment was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return layout      

def generateAddRoomBookingLayout(data):
    tableRows =[]

    for currClass in data:
        event_id, room_used, noOfAttendees, start_time, end_time = currClass
        currRow = html.Tr([html.Td(event_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(noOfAttendees,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle)])
        tableRows.append(currRow)

    
    addBookingLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('All Current Classes: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Event ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Number Of Attendees', style=columnStyle),
                            html.Th('Start Time', style=columnStyle),
                            html.Th('End Time', style=columnStyle),
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
                                html.Td(html.Label('Room to use:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='roomUsedInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Number of Attendees:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='noOfAttendeesInput', type='number',style=textFieldStyle2))
                            ]),                            
                            html.Tr([
                                html.Td(html.Label('Start Time HH:MM::SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='startInput', type='text',style=textFieldStyle2)),
                            ]),  
                            html.Tr([
                                html.Td(html.Label('End Time HH:MM:SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='endInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Submit', id='submitStaffAddBookingButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
            ), #second div
            dcc.ConfirmDialog(
            id='staffAddBookingSuccessful',
            message='Creating Room Booking was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return addBookingLayout

def roomBookingTable(data):
    tableRows =[]

    for currClass in data:
        event_id, room_used, noOfAttendees, start_time, end_time = currClass
        currRow = html.Tr([html.Td(event_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(noOfAttendees,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle)])
        tableRows.append(currRow)
        html.Div(
                id='tableContainer',
                children=[
                    html.Label('All Current Classes: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Event ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Number Of Attendees', style=columnStyle),
                            html.Th('Start Time', style=columnStyle),
                            html.Th('End Time', style=columnStyle),
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
                                html.Td(html.Label('Room to use:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='roomUsedInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Number of Attendees:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='noOfAttendeesInput', type='number',style=textFieldStyle2))
                            ]),                            
                            html.Tr([
                                html.Td(html.Label('Start Time HH:MM::SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='startInput', type='text',style=textFieldStyle2)),
                            ]),  
                            html.Tr([
                                html.Td(html.Label('End Time HH:MM:SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='endInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Submit', id='submitStaffAddBookingButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
        ),            

    return roomBookingTable

def generatePrintAllPayments(data):
    tableRows =[]

    for currPayment in data:
        payment_id, amount, member_email, transaction_date, stat,descript = currPayment
        currRow = html.Tr([html.Td(payment_id,style=dataStyle), 
                               html.Td(amount,style=dataStyle), 
                               html.Td(member_email,style=dataStyle), 
                               html.Td(transaction_date,style=dataStyle),
                               html.Td(stat,style=dataStyle),
                               html.Td(descript,style=dataStyle),
                                ])
        tableRows.append(currRow)

        layout = html.Div(
                id='tableContainer',
                children=[
                    html.Label('History Of All Payments: ', style={'fontSize': '30px'}),
                    html.Br(),
                    html.Br(),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Payment ID', style=columnStyle),  
                            html.Th('Amount ($)', style=columnStyle),
                            html.Th('Member Email', style=columnStyle),
                            html.Th('Transaction Date', style=columnStyle),
                            html.Th('Status', style=columnStyle),
                            html.Th('Description', style=columnStyle),
                        ])),
                        html.Tbody(id='classTableBody',children=tableRows),
                        ],

                        style={'margin': 'auto', 'border': '2px solid #ddd', 'textAlign': 'center', 'width': '100%'}  
                    ),
                    html.Div(
                        children=[
                            html.Br(),
                            html.Br(),                            
                            html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})

                        ]
                    )#second div end
                ],
                style={'textAlign': 'center'}  
            ),  #div end

    
    return layout
