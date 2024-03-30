
from dash import html,dcc

#this is the page for if the customer wnats to update the page
'''
	email VARCHAR(255) NOT NULL,
	first_name VARCHAR(15) NOT NULL,
	age INTEGER check (age > 0),
	gender VARCHAR(15) NOT NULL,
	height INTEGER check (height>0),
	weight INTEGER  check (weight>0),
	target_weight INTEGER check(target_weight>0),
	exercise_routine TEXT,
    
    '''
values = [('johnAdams@gmail.com','John',20,'male',150,50,60,'something')]
def generateLayout(values):
    return  html.Div([
        html.H1("Editable Text Fields"),
        dcc.Input(id='email', type='text', value=values[0][0]),
        dcc.Input(id='first_name', type='text', value=values[0][1]),
        dcc.Input(id='age', type='text', value=str(values[0][2])),
        dcc.Input(id='gender', type='text', value=values[0][3]),
        dcc.Input(id='height', type='text', value=str(values[0][4])),
        dcc.Input(id='weight', type='text', value=str(values[0][5])),
        dcc.Input(id='target_weight', type='text', value=str(values[0][6])),
        dcc.Input(id='exercise_routine', type='text', value=values[0][7]),      
        html.Div(id='output-message')
    ])
# import dash
# from dash import dcc, html, Input, Output, State

# # Sample data
# data = [("john", "pass1", 34, "A")]

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the Dash app
# app.layout = html.Div([
#     html.H1("Editable Text Fields"),
#     dcc.Input(id='username', type='text', value=data[0][0]),
#     dcc.Input(id='password', type='text', value=data[0][1]),
#     dcc.Input(id='age', type='text', value=str(data[0][2])),
#     dcc.Input(id='grade', type='text', value=data[0][3]),
#     html.Button('Submit Changes', id='submitChangeButton', n_clicks=0, style={'fontSize': 20}),
#     html.Div(id='output-message')
# ])

# @app.callback(
#     Output('output-message', 'children'),
#     Input('submitChangeButton', 'n_clicks'),
#     [State('username', 'value'),
#      State('password', 'value'),
#      State('age', 'value'),
#      State('grade', 'value')]
# )
# def update_data(n_clicks,username, password, age, grade):
#     new_data=[]
#     if n_clicks:
#         new_data.append(username)
#         new_data.append(password)
#         new_data.append(age)
#         new_data.append(grade)
#         print(new_data)
#         return f"Updated Data: {username}, {password}, {age}, {grade}"
#     else:
#         dash.no_update

# # Run the Dash app
# if __name__ == '__main__':
#     app.run_server(debug=True)
