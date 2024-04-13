from dash import  html,dcc

rowStyle = {'fontSize':'15px','textAlign': 'center', 'width':'180px','height':'80px'}
dataStyle = {'fontSize':'18px', 'color': 'blue'}
textFieldStyle2 = {'width': '70%', 'height': '30px'}
columnStyle = {'fontSize':'20px','padding': '15px'}
textFieldStyle ={'width': '100%', 'height': '30px'}

#layout for the main buttons
def mainLayout(name):
    mainLayout = html.Div(
        id = 'welcomeLayout',
        children=[
        
        html.Div(
            id = 'buttonsTable',
            children=[
            html.H1([
                html.Span('Hello Staff ',style={'color':'black'}),
                html.Span(name,style={'color':'#52489C'}),
                html.Span('!',style={'color':'black'}),
            ]),#heading done
            html.H1('Welcome to the Health and Fitness Club!'),
            html.Table([
                html.Tr([
                    html.Td(html.Button('Add Class', id='addClassButton', n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('Remove Class',id='removeClassButton',n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('Modify Class', id='modifyClassButton', n_clicks=0, style=rowStyle))
                ]), 
                html.Tr([
                    html.Td(html.Button('Add Room Booking', id='addRoomBookingButton', n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('Remove Room Booking',id='removeRoomBookingButton',n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('Modify Room Booking', id='modifyRoomBookingButton', n_clicks=0, style=rowStyle))
                ]),               
                html.Tr([
                    html.Td(html.Button('Print & Update Maintenance Checks',id='printMaintenanceButton',n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('Add Equipment Check', id='addEquipmentButton', n_clicks=0, style=rowStyle)),
                    html.Td(html.Button('Print History Of Payments', id='printReceiptButton', n_clicks=0, style=rowStyle)),

                ]),   
                html.Tr([
                    html.Td( html.Button('Add a new Payment', id='addNewPaymentButton', n_clicks=0, style = rowStyle)),
                    html.Td(html.Button('Update A Member Payment', id='updatePaymentButton', n_clicks=0, style=rowStyle)),
                    html.Td( html.Button('Go Back To Log In Page', id='typeMemberReturnButton', n_clicks=0, style = rowStyle),colSpan=3,style={'textAlign': 'center'})

                ]),                   
            ], style = {'margin':'auto'}
            ) #end of table
        ])#end of div
    ])
    return mainLayout

def generateRemoveClassLayout(data):
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
        schedule_id, room_used, trainer_email, day, start_time, end_time, session_type, class_type = currClass
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
        schedule_id, room_used, trainer_email, day,start_time, end_time, session_type, class_type = currClass
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
                                html.Td(html.Label('Room to use:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='roomUsedInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Trainer Email:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='trainerInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('On Day',style={'fontSize':'20px'})),
                                html.Td(dcc.DatePickerSingle(
                                            id='datePickedInput',
                                            min_date_allowed='2020-12-01',
                                            max_date_allowed='2026-12-31',
                                            initial_visible_month='2024-04-01',
                                            display_format='YYYY-MM-DD',  # Set the display format to YYYY-MM-DD
                                        )),
                            ]),                              
                            html.Tr([
                                html.Td(html.Label('Start Time HH:MM::SS: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='startInput', type='text',style={**textFieldStyle2,'margin-top':'10px'})),
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
                html.Td(dcc.Input(id='equipmentInRoomInput', type='text',style=mainStyle))
                ]),
                html.Tr([
                    html.Td(),
                    html.Td( html.Button('Add Equipment', id='submitAddEquipmentButton', n_clicks=0, style={**mainStyle,'width':'70%','height':'40px'})),                                 
                ]),                  
                html.Tr([
                    html.Td(),
                    html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0,  style={**mainStyle,'width':'70%','height':'40px'})),                                 
                ])  
            ]),            

            dcc.ConfirmDialog(
            id='staffaddEquipmentSuccessful',
            message='Adding of equipment was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return layout      

def generatePrintMaintenance(data):
    tableRows =[]

    for currMaintenance in data:
        equipment_ID, equipment_name, room_ID, last_checked = currMaintenance
        currRow = html.Tr([html.Td(equipment_ID,style=dataStyle), 
                               html.Td(equipment_name,style=dataStyle), 
                               html.Td(room_ID,style=dataStyle), 
                               html.Td(last_checked,style=dataStyle),
                            ])
        tableRows.append(currRow)

        layout = html.Div(
                id='page-content',
                children=[
                    html.Label('All Equipments and their last Date checked: ', style={'fontSize': '30px'}),
                    html.Br(),
                    html.Br(),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Equipment ID', style=columnStyle),  
                            html.Th('Equipment Name', style=columnStyle),
                            html.Th('In Room', style=columnStyle),
                            html.Th('Last Checked', style=columnStyle),
                        ])),
                        html.Tbody(id='classTableBody',children=tableRows),
                        ],

                        style={'margin': 'auto', 'border': '2px solid #ddd', 'textAlign': 'center', 'width': '100%'}  
                    ),
                    html.Div(
                        children=[
                            html.Table([
                            html.Tr([
                                html.Td(html.Label('In Room:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='roomInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Equipment Name:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='equipmentNameInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Submit', id='staffUpdateEquipmentButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                        ]),
                        html.Div(id='staffUpdateEquipmentOutcome'),
                        dcc.ConfirmDialog(
                        id='staffUpdateEquipmentSuccessful',
                        message='Updating Date of equipment check was successful. Will return back to main menu.',
                        ),                              
                        ],
                        style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'}
                    )#second div end
                ],
                style={'textAlign': 'center'}  
            ),  #div end

    
    return layout    

def generateAddRoomBookingLayout(data):
    tableRows =[]

    for currClass in data:
        event_id, room_used, noOfAttendees, day,start_time, end_time = currClass
        currRow = html.Tr([html.Td(event_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(noOfAttendees,style=dataStyle), 
                               html.Td(day,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle)])
        tableRows.append(currRow)

    
    addBookingLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('All Current Room Bookings: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Event ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Number Of Attendees', style=columnStyle),
                            html.Th('On Day', style=columnStyle),
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
                                html.Td(html.Label('On Day',style={'fontSize':'20px'})),
                                html.Td(dcc.DatePickerSingle(
                                            id='datePickedInput',
                                            min_date_allowed='2020-12-01',
                                            max_date_allowed='2026-12-31',
                                            initial_visible_month='2024-04-01',
                                            display_format='YYYY-MM-DD',  # Set the display format to YYYY-MM-DD
                                        )),
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
            html.Div(id='addRoomBookingOutcome'),
            dcc.ConfirmDialog(
            id='staffAddBookingSuccessful',
            message='Creating Room Booking was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return addBookingLayout

def generateRemoveRoomBookingLayout(data):
    tableRows =[]

    for currClass in data:
        event_id, room_used, noOfAttendees,day, start_time, end_time = currClass
        currRow = html.Tr([html.Td(event_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(noOfAttendees,style=dataStyle), 
                               html.Td(day,style=dataStyle), 
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle)])
        tableRows.append(currRow)

    
    removeBookingLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('All Current Room Bookings: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Event ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Number Of Attendees', style=columnStyle),
                            html.Th('On Day', style=columnStyle),
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
                                html.Td(html.Label('Event ID:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='eventToRemoveInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Remove', id='submitStaffRemoveBookingButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
            ), #second div
            html.Div(id='removeRoomBookingOutcome'),
            dcc.ConfirmDialog(
            id='staffRemoveBookingSuccessful',
            message='Removing Room Booking was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return removeBookingLayout

def generateModifyRoomBookingLayout(data):
    tableRows =[]

    for currClass in data:
        event_id, room_used, noOfAttendees,day, start_time, end_time = currClass
        currRow = html.Tr([html.Td(event_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(noOfAttendees,style=dataStyle), 
                               html.Td(day,style=dataStyle),
                               html.Td(start_time,style=dataStyle),
                                html.Td(end_time,style=dataStyle)])
        tableRows.append(currRow)

    
    modifyBookingLayout = html.Div(
        id='page-content',
        children=[
            html.Div(
                id='tableContainer',
                children=[
                    html.Label('All Current Room Bookings: ', style={'fontSize': '30px'}),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Event ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Number Of Attendees', style=columnStyle),
                            html.Th('On Day', style=columnStyle),
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
                                html.Td(html.Label('Event ID:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='StaffeventIdInput', type='text', placeholder='Enter Event ID',style=textFieldStyle2))
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
                                html.Td(html.Button('Submit', id='submitModifyRoomButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
            ), #second div
            html.Div(id='staffModifyRoomOutcome'),
            dcc.ConfirmDialog(
            id='staffmodifyRoomSuccessful',
            message='Modifying Room Booking was successful. Will return back to main menu.',
            ),    
    
    ]#children ends
    )
    return modifyBookingLayout        
         
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
                id='page-content',
                children=[
                    html.Label('History Of All Payments: ', style={'fontSize': '30px'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dcc.Input(id='filterEmailInput', type='text', placeholder='Enter email of Member to search', style={'margin-bottom': '10px','marginRight':'10px','height':'35px','width':'35%','fontSize':'20px'}),
                        html.Button('Filter', id='filterButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px',}),
                        html.Button('Clear Filters', id='clearFilterButton', n_clicks=0, style={'marginLeft':'10px','font-size': '16px', 'padding': '10px 20px',}),
                    ]),
                    html.Div(id='filterOutcome'),
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
                    )#second div end,

                ],
                style={'textAlign': 'center'}  
            ),  #div end

    
    return layout

def generateUpdatePayment(data):
    dropdownOptions = [
        {'label': 'Cancel Payment', 'value': 'CANCELED'},
        {'label': 'Complete Payment', 'value': 'COMPLETED'}        
    ]
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
                id='page-content',
                children=[
                    html.Label('All Payments: ', style={'fontSize': '30px'}),
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
                    html.Br(),
                    html.Br(),
                    html.Table([
                        html.Tr([
                            html.Td(html.Label('Enter Payment ID:', style={'fontSize': '20px'})),
                            html.Td(dcc.Input(id = 'paymentID',style={**textFieldStyle,'marginRight':'20px'})),
                            html.Td(dcc.Dropdown(id='staffPaymentStatus', options=dropdownOptions, style={**textFieldStyle2,'marginLeft':'10px','width':'150px'})),

                        ]),
                        html.Br(),
                        html.Tr([
                            html.Td(),
                            html.Td(),
                            html.Td(html.Button('Submit Status', id='staffPayStatusChangeButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px','marginLeft':'20px'})),
                        ]),
                        html.Tr([
                            html.Td(),
                            html.Td(),
                            html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px','marginLeft':'10px'})),
                        ]),
                    ]),
                    html.Div(id='staffUpdatePaymentOutcome'),
                    dcc.ConfirmDialog(
                    id='staffUpdatePaymentSuccessful',
                    message='Updating payment was successful. Will return back to main menu.',
                    ),
                ],
                style={'textAlign': 'center'}  
            ),  #div end

    return layout

def generateAddPaymentLayout():
    layout = html.Div(
        id = 'page-content',
        children = [
            html.H1("Add A New Payment:",style={'fontSize': '30px'}),
                    html.Table([
                            html.Tr([
                                html.Td(html.Label('Amount ($):',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='amountInput', type='text',style=textFieldStyle2))
                            ]),
                            html.Tr([
                                html.Td(html.Label('Member Email:',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='memberInput', type='text',style=textFieldStyle2))
                            ]),                            
                            html.Tr([
                                html.Td(html.Label('Transaction Date (YYYY-MM-DD): ',style={'fontSize':'20px'})),
                                html.Td(dcc.DatePickerSingle(
                                            id='dateInput',
                                            min_date_allowed='2020-12-01',
                                            max_date_allowed='2026-12-31',
                                            initial_visible_month='2024-04-01',
                                            display_format='YYYY-MM-DD',  # Set the display format to YYYY-MM-DD
                                        )),
                            ]),  

                            html.Tr([
                                html.Td(html.Label('Description of payment: ',style={'fontSize':'20px'})),
                                html.Td(dcc.Input(id='descriptionInput', type = 'text', style=textFieldStyle2))
                            ]),    
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Submit', id='submitStaffAddPaymentButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})), 
                            ]),
                            html.Tr([
                                html.Td(),
                                html.Td(html.Button('Go Back', id='staffReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})),                                 
                            ])  
                    ]),
                    html.Div(id='staffAddPaymentOutcome'),
                    dcc.ConfirmDialog(
                    id='staffAddPaymentSuccessful',
                    message='Adding of payment was successful. Will return back to main menu.',
                    ),

            ],style={'margin-bottom': '10px', 'width': '100%','display': 'flex', 'justify-content': 'center','flex-direction':'column','align-items': 'center'},
    ) #main div
 
    return layout