import dash
from dash import html,dcc,callback
from dash.dependencies import Input, Output, State

dash.register_page(__name__)

globalUsername  = ''
globalType = ''
globalFirstName = ''


import pages.memberLayouts as member
import pages.trainerLayouts as trainer
import pages.staffLayouts as staff
from pages.main import layout as mainPageLayout

import buttonHandler as handler
textFieldStyle ={'width': '100%', 'height': '30px','fontSize': '20px'}
buttonStyle = {'width': '100%', 'height': '50px', 'fontSize': '24px', 'margin': '10px auto'}
center={'display': 'flex', 'justify-content': 'center', 'align-items': 'center','height': '100vh'}

#layout for user log in
layout = html.Div(
        id='page-content',
        children=[
            dcc.Location(id='url',refresh=False),
            html.Div(
                    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'},
                    
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
            global globalUsername, globalType,globalFirstName
            globalUsername = username
            globalType = memberType


            #now to validate if it exits
            #need to create like a statement thing of whcih "welcome" it opens to  TO DO
            outcome,globalFirstName = handler.validateUser(username,password,memberType)
            if (outcome):
                
                if(memberType == 'members'):
                    new_url = 'members'
                    return member.mainLayout(globalFirstName),dash.no_update,new_url
                elif (memberType == 'trainer'):
                    new_url = 'trainer'
                    return trainer.mainLayout(globalFirstName),dash.no_update,new_url
                elif(memberType == 'admin_staff'):
                    new_url = 'admin'
                    return staff.mainLayout(globalFirstName),dash.no_update,new_url
                                
                
                #not validated
            else:
                return dash.no_update,"Incorrect. Please try again." ,'/login'

@callback(
    Output('url','pathname',allow_duplicate=True),
    Output('page-content','children',allow_duplicate=True),
    Input('logInReturnButton','n_clicks'),
    prevent_initial_call = True
)   

def backToMain(n_clicks):
    if n_clicks:
        return '/',mainPageLayout
    else:
        return dash.no_update,dash.no_update
  
#depending on the type of member they can go back to the login page
@callback(
    Output('page-content','children',allow_duplicate=True),
    Input('typeMemberReturnButton','n_clicks'),
    prevent_initial_call= True
)
def backToLogin(n_clicks):
    if n_clicks:
        return layout
    else:
        return dash.no_update
    
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
        return member.joinClassLayout(handler.printAvailableClasses())
    else:
        dash.no_update

#second function to actually join
@callback(
    Output('joinSuccessful','displayed',allow_duplicate=True),
    Output('page-content', 'children',allow_duplicate=True),
    Input('submitJoinButton','n_clicks'),
    State('scheduleIdInput', 'value'),
    prevent_initial_call = True
)

def joinClass(n_clicks,scheduleID):
    if n_clicks:
        print(scheduleID)
        if(scheduleID):
            handler.joinClass(scheduleID,globalUsername)
            return True,member.mainLayout(globalFirstName)
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
        return member.cancelClassLayout(handler.printMembersClass(globalUsername))
    else:
        return dash.no_update

#second function to actually cancel
@callback(
    Output('cancelSuccessful','displayed',allow_duplicate=True),
    Output('page-content','children'),
    Input('submitCancelButton','n_clicks'),
    State('scheduleIdInput','value'),
    prevent_initial_call = True
)

def cancelClass(n_clicks,scheduleID):
    if (n_clicks):
        if(scheduleID):
            handler.cancelClass(scheduleID,globalUsername)
            return True,member.mainLayout(globalFirstName)
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
        return True,member.mainLayout(globalFirstName)
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
        
#to generate the reschedule template
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('rescheduleClassButton', 'n_clicks'),
    prevent_initial_call=True
)
def reschedule_class(n_clicks):
    if n_clicks:
        return member.generateRescheduleClassLayout(handler.printSoloClass(globalUsername))
    else:
        return dash.no_update
    
#second function to actually reschedule
@callback(
    Output('rescheduleSuccessful','displayed',allow_duplicate=True),
    Output('rescheduleOutcome','children'),
    Output('page-content','children',allow_duplicate=True),
    Input('submitRescheduleButton','n_clicks'),
    State('scheduleIdInput','value'),
    State('startInput','value'),
    State('endInput','value'),
    prevent_initial_call = True
)

def reschedule_class(n_clicks,scheduleID,newStart,newEnd):
    if (n_clicks):
        if(scheduleID and newStart and newEnd):
            if(handler.rescheduleClass(scheduleID,newStart,newEnd)):
                #successful reschedule
                return True,dash.no_update,member.mainLayout(globalFirstName)
            else:
                #failed reschedule
                return False,'Reschdule Failed. There is an overlap. Please Try again.',dash.no_update
        #if all 3 values arent filled
        else:
            return False,dash.no_update,dash.no_update
    else:
        
        return False,dash.no_update,dash.no_update 
    
#to generate the view my payments layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('viewPaymentButton', 'n_clicks'),
    prevent_initial_call=True
)
def viewMyPayments(n_clicks):
    if n_clicks:
        #member.generateViewPayments(handler.printMyPayments(globalUsername))
        return member.generateDesignViewPayments(handler.printMyPayments(globalUsername))
    else:
        return dash.no_update

#functionality to payment
@callback(
    Output('memberPaySuccessful','displayed'),
    Output('payReceiptOutcome','children'),
    Output('page-content','children',allow_duplicate=True),
    Input('payReceiptButton','n_clicks'),
    State('payReceiptInput','value'),
    prevent_initial_call= True
)
def payReceipt(n_clicks,receiptToPay):
    if n_clicks:
        if(receiptToPay):
            if(handler.changePaymentStatus(receiptToPay,'COMPLETED')):
                return True,dash.no_update,member.mainLayout(globalFirstName)
            else:
                return False,'Error Paying Receipt. Please try again.',dash.no_update
        else:
            return False,dash.no_update,dash.no_update
  
#the return "go back" to the main page button  
@callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('goBackButton', 'n_clicks'),
    prevent_initial_call=True
)
def printDashboard(n_clicks):
    if n_clicks:
        return member.mainLayout(globalFirstName)
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


#submit button in trainer = > get member layout called
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

#update Availability
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('updateAvailabilityButton', 'n_clicks'),
    prevent_initial_call=True
)
def getMember(n_clicks):
    if n_clicks:
        return trainer.updateAvailabilityLayout
    else:
        return dash.no_update
    
#function that deals with "submit being clicked"
@callback(
    Output('updateAvailabilitySuccessful', 'displayed',allow_duplicate=True),
    Output('page-content', 'children', allow_duplicate=True),
    Output('updateAvailbiltyOutcome', 'children', allow_duplicate=True),
    Input('submitUpdateAvailabilityButton', 'n_clicks'),
    State('newTrainerStartInput','value'),
    State('newTrainerEndInput','value'),

    prevent_initial_call=True
)
def changeAvailability(n_clicks,newStart,newEnd):
    if n_clicks:
        #both filled
        if(newStart and newEnd):
            #change is good
            if(handler.setAvailability(globalUsername,newStart,newEnd)):
                return True,trainer.mainLayout(globalFirstName),dash.no_update
            else:
                #cant change
                return False,dash.no_update,'New Availabilty conflicts with current classes.'
        else:
            #not filled
            return False,dash.no_update

    else:
        return False,dash.no_update

#generate the view trainer class layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('viewTrainerClassButton', 'n_clicks'),
    prevent_initial_call=True
)
def trainerViewClass(n_clicks):
    if n_clicks:
        return trainer.generateViewMyClass(handler.trainerClasses(globalUsername))

#generate the notifications
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('viewNotificationButton', 'n_clicks'),
    prevent_initial_call=True
)
def trainerViewClass(n_clicks):
    if n_clicks:
        return trainer.generateNotificationLayout(handler.getNotifications(globalUsername))

#create functionality for the view notification button
@callback(
    Output('deleteNotificationsSuccessful','displayed'),
    Output('page-content','children',allow_duplicate=True),
    Input('trainerViewNotifications','n_clicks'),
    prevent_initial_call=True
)
def deleteNotifications(n_clicks):
    if n_clicks:
        if(handler.deleteNotifications(globalUsername)):
            return True,trainer.mainLayout(globalFirstName)
        else:
            return False,dash.no_update
    else:
        return False,dash.no_update
      
#the return "go back" to the main page button  
@callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('trainerReturnButton', 'n_clicks'),
    prevent_initial_call=True
)
def trainerGoBack(n_clicks):
    if n_clicks:
        return trainer.mainLayout(globalFirstName)
    else:
        return dash.no_update
    
'''STAFF VIEW'''

#generate an add class layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('addClassButton', 'n_clicks'),
    prevent_initial_call=True
)
def addClass(n_clicks):
    if n_clicks:
        return staff.generateAddClassLayout(handler.printAllClasses())
    else:
        return dash.no_update
#add class functionality
@callback(
    Output('staffAddClassSuccessful', 'displayed',allow_duplicate=True),
    Output('page-content', 'children', allow_duplicate=True),
    Output('staffAddClassOutcome', 'children', allow_duplicate=True),
    Input('submitStaffAddClassButton', 'n_clicks'),
    State('roomUsedInput','value'),
    State('trainerInput','value'),
    State('startInput','value'),
    State('endInput','value'),
    State('sessionTypeInput','value'),
    State('description','value'),

    prevent_initial_call=True
)
def add_class(n_clicks,roomUsed,trainerEmail,start_time,end_time,type_session,class_type):
    if n_clicks:
        #both filled
        if(roomUsed and trainerEmail and start_time and end_time and type_session and class_type):
            #change is good
            if(handler.staffAddClass(roomUsed,trainerEmail,start_time,end_time,type_session,class_type)):
                return True,staff.mainLayout(globalFirstName),dash.no_update
            else:
                #cant change
                return False,dash.no_update,'Class Conflicts. Please Try again.'
        else:
            #not filled
            return False,dash.no_update

    else:
        return False,dash.no_update
    
#generate a remove class layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('removeClassButton', 'n_clicks'),
    prevent_initial_call=True
)
def removeClass(n_clicks):
    if n_clicks:
        return staff.generateRemoveClassLayout(handler.printAllClasses())
    else:
        return dash.no_update
#remove class functionality 
@callback(
    Output('staffRemoveClassSuccessful', 'displayed',allow_duplicate=True),
    Output('page-content', 'children', allow_duplicate=True),
    Input('submitStaffRemoveClassButton', 'n_clicks'),
    Input('classToRemoveInput','value'),
    prevent_initial_call=True
)
def remove_class(n_clicks,scheduleID):
    if n_clicks:
        if(scheduleID):
            handler.staffRemoveClass(scheduleID)
            return True,staff.mainLayout(globalFirstName)
    
    else:
        return False,dash.no_update
       
#generate a modify class layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('modifyClassButton', 'n_clicks'),
    prevent_initial_call=True
)
def modifyClass(n_clicks):
    if n_clicks:
        return staff.generateModifyClassLayout(handler.printAllClasses())
    else:
        return dash.no_update
    
#modify class functionality
@callback(
    Output('staffmodifyClassSuccessful','displayed',allow_duplicate=True),
    Output('staffModifyClassOutcome','children'),
    Output('page-content','children',allow_duplicate=True),
    Input('submitModifyClassButton','n_clicks'),
    State('StaffscheduleIdInput','value'),
    State('StaffstartInput','value'),
    State('StaffendInput','value'),
    prevent_initial_call = True
)

def modify_class(n_clicks,scheduleID,newStart,newEnd):
    if (n_clicks):
        if(scheduleID and newStart and newEnd):
            if(handler.rescheduleClass(scheduleID,newStart,newEnd)):
                #successful reschedule
                return True,dash.no_update,staff.mainLayout(globalFirstName)
            else:
                #failed reschedule
                return False,'Reschdule Failed. There is an overlap. Please Try again.',dash.no_update
        #if all 3 values arent filled
        else:
            return False,dash.no_update,dash.no_update
    else:
        
        return False,dash.no_update,dash.no_update 
    
#generate a print maintence layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('printMaintenanceButton', 'n_clicks'),
    prevent_initial_call=True
)
def printMaintenance(n_clicks):
    if n_clicks:
        return staff.generatePrintMaintenance(handler.printAllMaintenance())
    else:
        return dash.no_update

#generate a update equipment check layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('updateMaintenanceButton', 'n_clicks'),
    prevent_initial_call=True
)
def updateMaintenance(n_clicks):
    if n_clicks:
        return staff.generateUpdateEquipmentLayout()
    else:
        return dash.no_update 

#update Equipment functionality
@callback(
    Output('staffUpdateEquipmentSuccessful','displayed',allow_duplicate=True),
    Output('staffUpdateEquipmentOutcome','children'),
    Output('page-content','children',allow_duplicate=True),
    Input('staffUpdateEquipmentButton','n_clicks'),
    State('equipmentNameInput','value'),
    prevent_initial_call = True
)

def update_equipment(n_clicks,equipmentName):
    if (n_clicks):
        if(equipmentName):
            if(handler.updateEquipment(equipmentName)):
                #successful update
                return True,dash.no_update,staff.mainLayout(globalFirstName)
            else:
                #failed update
                return False,'Error Updating equipment!',dash.no_update
       
        #if values arent filled
        else:
            return False,dash.no_update,dash.no_update
    else:
        
        return False,dash.no_update,dash.no_update 
    

#generate an add equipment layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('addEquipmentButton', 'n_clicks'),
    prevent_initial_call=True
)
def addEquipment(n_clicks):
    if n_clicks:
        return staff.generateAddEquipmentLayout()
    else:
        return dash.no_update 
    
#functionality for add equipment
@callback(
    Output('staffaddEquipmentSuccessful','displayed',allow_duplicate=True),
    Output('page-content','children',allow_duplicate=True),
    Input('submitAddEquipmentButton','n_clicks'),
    State('newEquipmentNameInput','value'),
    State('equipmentInRoomInput','value'),
    prevent_initial_call = True
)

def add_equipment(n_clicks,equipmentName,inRoom):
    print("in room")
    print(inRoom)
    if (n_clicks):
        if(equipmentName and inRoom):
            if(handler.addEquipment(equipmentName,inRoom)):
                #successful adding
                return True,staff.mainLayout(globalFirstName)
            else:
                #failed adding
                return False,dash.no_update
        
        #if all 2 values arent filled
        else:
            return False,dash.no_update
    else:
        
        return False,dash.no_update 
    

#generate a add room booking layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('addRoomBookingButton', 'n_clicks'),
    prevent_initial_call=True
)
def addRoomBooking(n_clicks):
    if n_clicks:
        #has to change to be print all room bookings COME BACK
        return staff.generateAddRoomBookingLayout(handler.printAllRoomBooking())
    else:
        return dash.no_update 

#functionality for add room
@callback(
    Output('staffAddBookingSuccessful','displayed',allow_duplicate=True),
    Output('addRoomBookingOutcome','children'),
    Output('page-content','children',allow_duplicate=True),
    Input('submitStaffAddBookingButton','n_clicks'),
    State('roomUsedInput','value'),
    State('noOfAttendeesInput','value'),
    State('startInput','value'),
    State('endInput','value'),    
    prevent_initial_call = True
)

def add_roomBooking(n_clicks,roomToUse,attendees,startTime,endTime):

    if (n_clicks):
        if(roomToUse and attendees and startTime and endTime):
            if(handler.addRoomBooking(roomToUse,attendees,startTime,endTime)):
                #successful adding
                return True,dash.no_update,staff.mainLayout(globalFirstName)
            else:
                #failed adding
                return False,'Reschdule Failed. There is an overlap. Please Try again.',dash.no_update
        
        #if all  values arent filled
        else:
            return False,dash.no_update
    else:
        
        return False,dash.no_update 
    
#generate a remove room booking layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('removeRoomBookingButton', 'n_clicks'),
    prevent_initial_call=True
)
def removeRoomBooking(n_clicks):
    if n_clicks:
        #has to change to be print all room bookings COME BACK
        return staff.generateRemoveRoomBookingLayout(handler.printAllRoomBooking())
    else:
        return dash.no_update
         
#functionality for remove room
@callback(
    Output('staffRemoveBookingSuccessful','displayed',allow_duplicate=True),
    Output('removeRoomBookingOutcome','children'),
    Output('page-content','children',allow_duplicate=True),
    Input('submitStaffRemoveBookingButton','n_clicks'),
    State('eventToRemoveInput','value'), 
    prevent_initial_call = True
)

def remove_roomBooking(n_clicks,eventToRemove):

    if (n_clicks):
        if(eventToRemove):
            if(handler.removeRoomBooking(eventToRemove)):
                #successful adding
                return True,dash.no_update,staff.mainLayout(globalFirstName)
            else:
                #failed adding
                return False,'Remove Failed. Please Try again.',dash.no_update
        
        #if all  values arent filled
        else:
            return False,dash.no_update
    else:
        
        return False,dash.no_update 

#generate a modify room booking layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('modifyRoomBookingButton', 'n_clicks'),
    prevent_initial_call=True
)

def modifyRoomBooking(n_clicks):
    if n_clicks:
        #has to change to be print all room bookings COME BACK
        return staff.generateModifyRoomBookingLayout(handler.printAllRoomBooking())
    else:
        return dash.no_update

#functionality modify room booking layout
@callback(
    Output('staffmodifyRoomSuccessful','displayed'),
    Output('page-content', 'children', allow_duplicate=True),
    Output('staffModifyRoomOutcome','children'),
    Input('submitModifyRoomButton', 'n_clicks'),
    State('StaffeventIdInput','value'),
    State('StaffstartInput','value'),
    State('StaffendInput','value'),
    prevent_initial_call=True
)
def modifyRoomBooking(n_clicks,eventID,startTime,endTime):
    if n_clicks:
        if(eventID and startTime and endTime):
            #all values there
            if(handler.modifyRoomBooking(eventID,startTime,endTime)):
                return True,staff.mainLayout(globalFirstName),dash.no_update
            else:
                #modify failed
                return False,dash.no_update,'Error: cannot modify room booking. Please Try again,'
        else:
            return False,dash.no_update,dash.no_update
    else:
        return dash.no_update


#generate a PRINT HISTORY OF ALL PAYMENTS layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('printReceiptButton', 'n_clicks'),
    prevent_initial_call=True
)
def printAllPayments(n_clicks):
    if n_clicks:
        #has to change to be print all room bookings COME BACK
        return staff.generatePrintAllPayments(handler.printAllPayments())
    else:
        return dash.no_update
    
#functionality for filter payments based on member email
@callback(
        [Output('page-content','children',allow_duplicate = True),
        Output('filterOutcome','children')],
        Input('filterButton','n_clicks'),
        State('filterEmailInput','value'),
        prevent_initial_call =  True
)
def filter_payment(n_clicks,email):
    if (n_clicks):
        if (email):
            outcome,values =handler.filterPayment(email)
            if outcome:
                return staff.generatePrintAllPayments(values),dash.no_update
            else:
                return dash.no_update,'Invalid Member Email. Please Try again.'
        else:
            return dash.no_update,dash.no_update
    else:
        return dash.no_update,dash.no_update

#functionality for clear filter payments 
@callback(
        [Output('page-content','children',allow_duplicate = True),
        Output('filterEmailInput','value')],
        Input('clearFilterButton','n_clicks'),
        prevent_initial_call =  True
)
def clearFilter_payment(n_clicks):
    if (n_clicks):
            return staff.generatePrintAllPayments(handler.printAllPayments()),''
    else:
        return dash.no_update,dash.no_update
        
#generate an update payment layout
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('updatePaymentButton', 'n_clicks'),
    prevent_initial_call=True
)
def updatePayment(n_clicks):
    if n_clicks:
        #has to change to be print all room bookings COME BACK
        return staff.generateUpdatePayment(handler.printAllPayments())
    else:
        return dash.no_update

#functionality for update payment Button
@callback(
        [Output('staffUpdatePaymentSuccessful','displayed'),
         Output('page-content','children',allow_duplicate = True),
        Output('staffUpdatePaymentOutcome','children')],
        Input('staffPayStatusChangeButton','n_clicks'),
        [State('paymentID','value'),
        State('staffPaymentStatus','value')],
        prevent_initial_call =  True
)
def update_payment(n_clicks,payment_id,newStatus):
    if (n_clicks):
        if (payment_id and newStatus):
            if(handler.changePaymentStatus(payment_id,newStatus)):
                return True,staff.mainLayout(globalFirstName),dash.no_update
            else:
                return False,dash.no_update,'Error Changing Status. Please try again.'
        
    else:
        return False,dash.no_update,dash.no_update

#generate an add payment layout   
@callback(
    Output('buttonsTable', 'children', allow_duplicate=True),
    Input('addNewPaymentButton', 'n_clicks'),
    prevent_initial_call=True
)
def addPayment(n_clicks):
    if n_clicks:
        return staff.generateAddPaymentLayout()
    else:
        dash.no_update

#functionality for add payment Button
@callback(
        [Output('staffAddPaymentSuccessful','displayed'),
         Output('page-content','children',allow_duplicate = True),
        Output('staffAddPaymentOutcome','children')],
        Input('submitStaffAddPaymentButton','n_clicks'),
        [State('amountInput','value'),
        State('memberInput','value'),
        State('dateInput','value'),
        State('descriptionInput','value')   
        ],
        prevent_initial_call =  True
)
def update_payment(n_clicks,amountID,memberEmail,date,desc):
    if (n_clicks):
        if (amountID and memberEmail and date and desc):
            if(handler.addPayment(amountID,memberEmail,date,'PENDING',desc)):
                return True,staff.mainLayout(globalFirstName),dash.no_update
            else:
                return False,dash.no_update,'Error Adding Payment. Please try again.'
        
    else:
        return False,dash.no_update,dash.no_update    
                
#the return "go back" to the main page button  
@callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('staffReturnButton', 'n_clicks'),
    prevent_initial_call=True
)
def staffReturn(n_clicks):
    if n_clicks:
        return staff.mainLayout(globalFirstName)
    else:
        return dash.no_update