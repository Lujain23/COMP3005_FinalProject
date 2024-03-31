from dash import  html,dcc
'''
addClass()
removeClass()
modifyClass()
printMaintenance() -> print statement of all items and the last time they were checked
addEquipment() -> adding the equipment that was checked, default date would be current date
updateMaintenanceCheck() -> update the maintenance date 
printReceipt()
'''
rowStyle = {'fontSize':'20px','textAlign': 'center', 'width':'200px','height':'100px'}
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
                html.Td(),
                html.Td(html.Button('Print Receipt', id='printReceiptButton', n_clicks=0, style=rowStyle))
            ]),  
                
        ], style = {'margin':'auto'}
        ) #end of table
    ])#end of div
])