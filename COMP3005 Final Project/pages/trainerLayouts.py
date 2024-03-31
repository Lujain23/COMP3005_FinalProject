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