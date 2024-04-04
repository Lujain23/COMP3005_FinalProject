from dash import  html,dcc
'''
setAvailiability() -> update availability of CURRENT trainer
getMember() -> select specific member (they have the name in their heads)
'''
rowStyle = {'fontSize':'20px','textAlign': 'center', 'width':'200px','height':'100px'}
textFieldStyle ={'width': '100%', 'height': '30px','fontSize': '20px'}
columnStyle = {'fontSize':'20px','padding': '15px'}
dataStyle = {'fontSize':'18px', 'color': 'blue'}

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
            html.Tr([
                html.Td(html.Button('View My Classes', id='viewTrainerClassButton', n_clicks=0, style=rowStyle)),
                html.Td(html.Button('View Notifications', id='viewNotificationButton', n_clicks=0, style=rowStyle))
            ]),
            html.Tr([
                html.Td( html.Button('Go Back', id='typeMemberReturnButton', n_clicks=0, style = rowStyle),colSpan=2,style={'textAlign': 'center'})
            ]),                                    
        ], style = {'margin':'auto'}
        ), #end of table
    ])#end of div
])

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
        ),
        html.Br(),
        html.Br(),
        html.Div(
            children=[
                html.Button('Go Back', id='trainerReturnButton',style={'textAlign': 'center','width': '20%', 'height': '50px','fontSize':'16px'})
            ],
            style = {'display': 'flex', 'justify-content': 'center'}
        )#end of button div
       
])

updateAvailabilityLayout = html.Div(
    id='page-content',
    children=[
         html.H1("Update Availability",style={'fontSize':'50px'}),
                        dcc.Input(id='newTrainerStartInput', type='text', placeholder='Enter new start Time HH:MM:SS',style=textFieldStyle),
                        html.Br(),
                        html.Br(),
                        dcc.Input(id='newTrainerEndInput', type='text', placeholder='Enter new end Time HH:MM:SS',style=textFieldStyle),
                        html.Br(),
                        html.Br(),
                        html.Button('Submit', id='submitUpdateAvailabilityButton',style={'textAlign': 'center','width': '100%', 'height': '50px','fontSize':'24px'}),
                        html.Br(),
                        html.Br(),
                        html.Button('Go Back', id='trainerReturnButton',style={'textAlign': 'center','width': '100%', 'height': '50px','fontSize':'24px'}),
                        dcc.ConfirmDialog(
                            id='updateAvailabilitySuccessful',
                            message='Updating availability was successful. Will return back to main menu.',
                        ),
                        html.Div(id='updateAvailbiltyOutcome')
    ]
)

def generateViewMyClass(data):
    tableRows =[]

    for currClass in data:
        schedule_id, room_used, start_time, end_time, type_session, class_type = currClass
        currRow = html.Tr([html.Td(schedule_id,style=dataStyle), 
                               html.Td(room_used,style=dataStyle), 
                               html.Td(start_time,style=dataStyle), 
                               html.Td(end_time,style=dataStyle),
                               html.Td(type_session,style=dataStyle),
                               html.Td(class_type,style=dataStyle),
                                ])
        tableRows.append(currRow)

        layout = html.Div(
                id='tableContainer',
                children=[
                    html.Label('My Classes: ', style={'fontSize': '30px'}),
                    html.Br(),
                    html.Br(),
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th('Schdule ID', style=columnStyle),  
                            html.Th('Room Used', style=columnStyle),
                            html.Th('Start Time', style=columnStyle),
                            html.Th('End Time', style=columnStyle),
                            html.Th('Session Type', style=columnStyle),
                            html.Th('Class Type', style=columnStyle),
                        ])),
                        html.Tbody(id='classTableBody',children=tableRows),
                        ],

                        style={'margin': 'auto', 'border': '2px solid #ddd', 'textAlign': 'center', 'width': '100%'}  
                    ),
                    html.Div(
                        children=[
                            html.Br(),
                            html.Br(),                            
                            html.Button('Go Back', id='trainerReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})

                        ]
                    )#second div end
                ],
                style={'textAlign': 'center'}  
            ),  #div end

    
    return layout

def generateNotificationLayout(data):
    notification = {
        'background-color': '#f8f9fa',  
        'border': '2px solid #dc3545',  
        'padding': '10px',              
        'margin-bottom': '15px',       
        'color': '#721c24',              
        'font-size': '20px'             
    }

    rows = []
    for currNotification in data:
        divNotification = html.Div(
                currNotification,style=notification 
        )
        rows.append(divNotification)    

    layout = html.Div(
        id='page-content',
        children=[
            html.Div(
                html.H1("My Notifications:",style={'fontSize': '30px'})
            ),
            html.Div(rows),
            html.Div([
                html.Button('Viewed', id = 'trainerViewNotifications',style={'font-size': '16px', 'padding': '10px 20px','margin-right': '10px'}),
                html.Button('Go Back', id='trainerReturnButton', n_clicks=0, style={'font-size': '16px', 'padding': '10px 20px'})
            ]),
            dcc.ConfirmDialog(
            id='deleteNotificationsSuccessful',
            message='You have viewed all notification and they have been deleted. Will return back to main menu.',
            ),            
        ]
    )
    return layout