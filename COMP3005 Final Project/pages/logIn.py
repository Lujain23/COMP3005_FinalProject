import dash
from dash import html,dcc,callback
from dash.dependencies import Input, Output, State

dash.register_page(__name__)

globalUsername  = ''
globalType = ''


import pages.memberLayouts as member
import pages.trainerLayouts as trainer
import pages.staffLayouts as staff

import buttonHandler as handler
textFieldStyle ={'width': '100%', 'height': '30px','fontSize': '20px'}
#layout for user log in
layout = html.Div(
     children=[
          dcc.Location(id='url',refresh=False),
          html.Div(
                style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'},
                id='page-content',
                children=[
                    html.Div([
                        html.H1("Log In Page",style={'fontSize':'50px'}),
                        dcc.Input(id='usernameInput', type='text', placeholder='Enter username',style=textFieldStyle),
                        html.Br(),
                        html.Br(),
                        dcc.Input(id='passwordInput', type='password', placeholder='Enter password',style=textFieldStyle),
                        html.Br(),
                        html.Br(),
                        dcc.Dropdown(
                            id='memberType',
                            options=[
                                {'label': 'Member', 'value': 'members'},
                                {'label': 'Trainer', 'value': 'trainer'},
                                {'label': 'Staff', 'value': 'admin_staff'}
                            ],
                            style=textFieldStyle

                        ),
                        html.Br(),
                        html.Br(),
                        html.Button('Submit', id='logInSubmitButton',style={'textAlign': 'center','width': '100%', 'height': '50px','fontSize':'24px'}),
                        html.Br(),
                        html.Br(),
                        html.Button('Go Back', id='logInReturnButton',style={'textAlign': 'center','width': '100%', 'height': '50px','fontSize':'24px'}),
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
            if (handler.validateUser(username,password,memberType)):
                
                if(memberType == 'members'):
                    new_url = 'members'
                    return member.mainLayout,dash.no_update,new_url
                elif (memberType == 'trainer'):
                    new_url = 'trainer'
                    return trainer.mainLayout,dash.no_update,new_url
                elif(memberType == 'admin_staff'):
                    new_url = 'admin'
                    return staff.mainLayout,dash.no_update,new_url
                                
                
                #not validated
            else:
                return dash.no_update,"Incorrect. Please try again." ,'/login'

''' MEMBER VIEW'''
#functions for the buttons for MEMBER
            
#join class 
#first function to generate the layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('joinClassButton', 'n_clicks'),
    prevent_initial_call=True
)
def join_class(n_clicks):
    if n_clicks:
        print(handler.printAvailableClasses())
        return member.classLayout(handler.printAvailableClasses(),'Available Classes:','Join Successful! Will go back to Main Menu.')
    else:
        dash.no_update

#second function to actually join
@callback(
    Output('successful','displayed',allow_duplicate=True),
    Output('page-content', 'children',allow_duplicate=True),
    Input('submitChangeButton','n_clicks'),
    State('scheduleIdInput', 'value'),
    prevent_initial_call = True
)

def joinClass(n_clicks,scheduleID):
    if n_clicks:
        if(scheduleID):
            handler.joinClass(scheduleID,globalUsername)
            return True,member.mainLayout
        else:
            False,dash.no_update
    else:
        
        return False,dash.no_update  


#cancel class
    #first function to generate the layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('cancelClassButton', 'n_clicks'),
    prevent_initial_call=True
)
def cancel_class(n_clicks):
    if n_clicks:
        print("CANCEL: ",handler.printMembersClass(globalUsername))
        return member.classLayout(handler.printMembersClass(globalUsername),'Enrolled Classes:','Cancel Successful! Will go back to Main Menu.')
    else:
        return dash.no_update

#second function to actually cancel
@callback(
    Output('page-content','children'),
    Input('submitChangeButton','n_clicks'),
    State('scheduleIdInput','value'),
    prevent_initial_call = True
)

def cancelClass(n_clicks,scheduleID):
    if (n_clicks):
        if(scheduleID):
            handler.cancelClass(scheduleID,globalUsername)
            return True,member.mainLayout
        else:
            False,dash.no_update
    else:
        
        return False,dash.no_update  

#first function to generate the textfields
@callback(
     Output('buttonsTable','children',allow_duplicate=True),
     Input('updateInfoButton','n_clicks'),
     prevent_initial_call = True
)

def update_information(n_clicks):
    if n_clicks:
        print("current user: ", globalUsername) #would have to change by getting the username value being used

        values = handler.selectMember(globalUsername)
 
        return member.generateLayout(values)
        
    else:
        return dash.no_update
    
# second function for when the update is called
@callback(
    Output('confirmUpdate','displayed'),
    Output('page-content', 'children',allow_duplicate=True),
    Input('updateButton','n_clicks'),
    State('emailInput', 'value'),
    State('passwordInput', 'value'),
    State('nameInput', 'value'),
    State('ageInput', 'value'),
    State('genderInput', 'value'),
    State('heightInput', 'value'),
    State('weightInput', 'value'),
    State('targetInput', 'value'),
    State('exerciseRoutineInput', 'value'),
    prevent_initial_call = True
)

def update_information_done(n_clicks,email,password,firstName,age,gender,height,weight,target,exceriseRoutine):
    if n_clicks:
        #will have to call the function that updates the values //SQL
        handler.updateMember(email,password,firstName,age,gender,height,weight,target,exceriseRoutine)
        return True,member.mainLayout 
    else:
        return False,dash.no_update    

#print dashboard
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('printDashboardButton', 'n_clicks'),
    prevent_initial_call=True
)
def printDashboard(n_clicks):
    if n_clicks:
        exercise_routine, height, weight, target_weight, BMI, isOverweight, weightChange, achievement = handler.printDashboard(globalUsername)
        return member.generatePrintDashboardLayout(exercise_routine, height, weight, target_weight, BMI, isOverweight, weightChange, achievement)
        

#the return "go back" to the main page button  
@callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('goBackButton', 'n_clicks'),
    prevent_initial_call=True
)
def printDashboard(n_clicks):
    if n_clicks:
        return member.mainLayout
    else:
        return dash.no_update
        

''' TRAINER VIEW'''
#get member button clicked
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('getMemberButton', 'n_clicks'),
    prevent_initial_call=True
)
def getMember(n_clicks):
    if n_clicks:
        return trainer.getMemberLayout


#submit button in get member layout called
@callback(
    Output('memberTableBody', 'children', allow_duplicate=True),
    Input('submitGetMemberButton', 'n_clicks'),
    State('nameInput','value'),
    prevent_initial_call=True
)
def submitGetMember(n_clicks,memberToSearch):
    dataStyle = {'fontSize':'18px', 'color': 'blue'}
    if n_clicks:
        data = []
        data = handler.getMember(memberToSearch)

        tableRows = [] 

        for currentMember in data:
            first_name, age, gender, height, weight, target_weight, exercise_routine = currentMember
            currRow = html.Tr([html.Td(first_name,style=dataStyle), 
                               html.Td(age,style=dataStyle), 
                               html.Td(gender,style=dataStyle), 
                               html.Td(height,style=dataStyle),
                                html.Td(weight,style=dataStyle), 
                                 html.Td(target_weight,style=dataStyle),
                                   html.Td(exercise_routine,style=dataStyle)])
            tableRows.append(currRow)

        return tableRows

'''STAFF VIEW'''