import dash
from dash import  html

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
layout = html.Div([
    html.H1('Welcome to the Health and Fitness Club!'),
    html.Div([
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
        ], style = {'paddingLeft':'100px'}
        ) #end of table
    ])#end of div
])