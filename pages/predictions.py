# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from joblib import load

# Imports from this application
from app import app

# Load pipeline
# pipeline = load('assets/pipeline.joblib')
pipeline = load('assets/pipeline.joblib')
print('Pipeline loaded!')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
        
#             ## Predictions

#             Your instructions: How to use your app to get new predictions.

#             """
#         ),

        

#         dcc.Slider(
#             id='slider1',
#             min=0,
#             max=100,
#             step=0.5,
#             value=0,
#             # marks={i: 'Label {}'.format(i) for i in range(10)},
#             marks = {0: '0',
#             20: '20',
#             40: '40',
#             60: '60',
#             80: '80',
#             100: '100'},
#             className = 'mb-5' #spacing between this and next text
#         ),

#         dcc.Markdown(id='output1')

#     ],
#     md=4,
# )


#  'neighborhood', 

#   'grade prior',
#  'score prior',
#  'violations prior',
#  'critical violations prior',

# ['persons_per_acre',
#  'female to male',
#  'adults to minor',

#  'inspection date year',
#  'inspection date month',
#  'inspection date day']


column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 

        dcc.Markdown('#### Neighborhood'), 
        dcc.Dropdown(
            id='neighborhood', 
            options = [
               
                {'label': 'Rockaways', 'value': 'Rockaways'},
                {'label': 'Jamaica', 'value': 'Jamaica'},
                {'label': 'Southeast Queens', 'value': 'Southeast Queens'},
                {'label': 'Southwest Queens', 'value': 'Southwest Queens'},
                {'label': 'West Central Queens', 'value': 'West Central Queens'},
                {'label': 'West Queens', 'value': 'West Queens'},
                {'label': 'Central Queens', 'value': 'Central Queens'},
                {'label': 'Northeast Queens', 'value': 'Northeast Queens'},
                {'label': 'North Queens', 'value': 'North Queens'},
                {'label': 'Canarsie and Flatlands', 'value': 'Canarsie and Flatlands'},
                {'label': 'Central Brooklyn', 'value': 'Central Brooklyn'},
                {'label': 'Bushwick and Williamsburg', 'value': 'Bushwick and Williamsburg'},
                {'label': 'Southern Brooklyn', 'value': 'Southern Brooklyn'},
                {'label': 'Sunset Park', 'value': 'Sunset Park'},
                {'label': 'Northwest Brooklyn', 'value': 'Northwest Brooklyn'},
                {'label': 'Borough Park', 'value': 'Borough Park'},
                {'label': 'Southwest Brooklyn', 'value': 'Southwest Brooklyn'},
                {'label': 'Flatbush', 'value': 'Flatbush'},
                {'label': 'Greenpoint', 'value': 'Greenpoint'},
                {'label': 'East New York and New Lots', 'value': 'East New York and New Lots'},
                {'label': 'Northwest Queens', 'value': 'Northwest Queens'},
                {'label': 'Northeast Bronx', 'value': 'Northeast Bronx'},
                {'label': 'Hunts Point and Mott Haven', 'value': 'Hunts Point and Mott Haven'},
                {'label': 'Southeast Bronx', 'value': 'Southeast Bronx'},
                {'label': 'Kingsbridge and Riverdale', 'value': 'Kingsbridge and Riverdale'},
                {'label': 'Bronx Park and Fordham', 'value': 'Bronx Park and Fordham'},
                {'label': 'Central Bronx', 'value': 'Central Bronx'},
                {'label': 'High Bridge and Morrisania', 'value': 'High Bridge and Morrisania'},
                {'label': 'Mid-Island', 'value': 'Mid-Island'},
                {'label': 'South Shore', 'value': 'South Shore'},
                {'label': 'Port Richmond', 'value': 'Port Richmond'},
                {'label': 'Stapleton and St. George', 'value': 'Stapleton and St. George'},
                {'label': 'Lower Manhattan', 'value': 'Lower Manhattan'},
                {'label': 'Upper East Side', 'value': 'Upper East Side'},
                {'label': 'Inwood and Washington Heights', 'value': 'Inwood and Washington Heights'},
                {'label': 'Central Harlem', 'value': 'Central Harlem'},
                {'label': 'Chelsea and Clinton', 'value': 'Chelsea and Clinton'},
                {'label': 'East Harlem', 'value': 'East Harlem'},
                {'label': 'Upper West Side', 'value': 'Upper West Side'},
                {'label': 'Gramercy Park and Murray Hill', 'value': 'Gramercy Park and Murray Hill'},
                {'label': 'Greenwich Village and Soho', 'value': 'Greenwich Village and Soho'},
                {'label': 'Lower East Side', 'value': 'Lower East Side'},

                
            ], 
            value = 'Lower Manhattan', 
            className='mb-5', 
        ),

        dcc.Markdown('#### Day of Week'), 
        dcc.Dropdown(
            id='inspection_date_dayofweek', 
            options = [
               
                {'label': 'Monday', 'value': 0},
                {'label': 'Tuesday', 'value': 1},
                {'label': 'Wednesday', 'value': 2},
                {'label': 'Thursday', 'value': 3},
                {'label': 'Friday', 'value': 4},
                {'label': 'Saturday', 'value': 5},
                {'label': 'Sunday', 'value': 6},
            ],
            value = 0, 
            className='mb-5', 
        ),

        dcc.Markdown('#### Month of Year'), 
        dcc.Dropdown(
            id='inspection_date_month', 
            options = [
               
                {'label': 'January', 'value': 1},
                {'label': 'February', 'value': 2},
                {'label': 'March', 'value': 3},
                {'label': 'April', 'value': 4},
                {'label': 'May', 'value': 5},
                {'label': 'June', 'value': 6},
                {'label': 'July', 'value': 7},
                {'label': 'August', 'value': 8},
                {'label': 'September', 'value': 9},
                {'label': 'October', 'value': 10},
                {'label': 'November', 'value': 11},
                {'label': 'December', 'value': 12},
                
            ],
            value = 6, 
            className='mb-5', 
        ),
        

        dcc.Markdown('#### Prior Grade'), 
        dcc.Dropdown(
            id='grade_prior', 
            options = [
               
                {'label': 'A', 'value': 'A'},
                {'label': 'B', 'value': 'B'},
                {'label': 'C', 'value': 'C'},
                            ], 
            value = 'A', 
            className='mb-5', 
        ),

        dcc.Markdown('#### Prior Score'), 
        dcc.Slider(
            id='score_prior', 
            min=0,
            max=100,
            value=11,
            step=1,
            marks={n: str(n) for n in range(10,101,10)}, 

            className='mb-5', 
        ), 

        dcc.Markdown('#### Prior Violations'), 
        dcc.Slider(
            id='violations_prior', 
            min=0,
            max=12,
            value=2,
            step=1,
            marks={n: str(n) for n in range(0,13)}, 

            className='mb-5', 
        ), 

        dcc.Markdown('#### Prior Critical Violations'), 
        dcc.Slider(
            id='critical_violations_prior', 
            min=0,
            max=8,
            value=2,
            step=1,
            marks={n: str(n) for n in range(0,9)}, 

            className='mb-5', 
        ), 



        dcc.Markdown('#### Persons Per Acre'), 
        dcc.Slider(
            id='persons_per_acre', 
            min=0,
            max=325,
            value=100,
            step=10,
            marks={n: str(n) for n in range(0,326,25)}, 

            className='mb-5', 
        ), 

        dcc.Markdown('#### Female-to-Male Ratio'), 
        dcc.Slider(
            id='female_to_male', 
            min=0,
            max=3,
            value=100,
            step=0.1,
            marks={n: str(n) for n in range(0,3)}, 

            className='mb-5', 
        ), 

        #TODO: update slider 
        dcc.Markdown('#### Adults-to-Minors Ratio'), 
        dcc.Slider(
            id='adults_to_minor', 
            min=0,
            max=100,
            value=8,
            step=.5,
            marks={n: str(n) for n in range(0,101,10)}, 

            className='mb-5', 
        ), 


         
    ],
    md=4,
)

# column2 = dbc.Col(
#     [
   
#         # daq.Gauge(
#         # id='my-daq-gauge',
#         # min=0,
#         # max=100,
#         # value=6
#         # )  

#     ]
# )

column2 = dbc.Col(
    [
        html.H2('Expected Grade - Fail probability', className='mb-5'), 
        html.Div(id='no-go-probability', className='lead')
    ]
)

 

layout = dbc.Row([column1, column2])

@app.callback(
    Output('no-go-probability', 'children'),
    [
        Input('neighborhood', 'value'),
        Input('grade_prior', 'value'),
        Input('score_prior', 'value'),
        Input('violations_prior', 'value'),
        Input('critical_violations_prior', 'value'),
        Input('persons_per_acre', 'value'),
        Input('female_to_male', 'value'),
        Input('adults_to_minor', 'value'),
        Input('inspection_date_month', 'value'),
        Input('inspection_date_dayofweek', 'value')
    ]
)

def predict(neighborhood,grade_prior, score_prior, violations_prior, critical_violations_prior,persons_per_acre,female_to_male,adults_to_minor, inspection_date_month,inspection_date_dayofweek):
    
    df = pd.DataFrame(
        columns=[ 'neighborhood','grade prior','score prior','violations prior','critical violations prior','persons_per_acre','female to male','adults to minor', 'inspection date month','inspection date dayofweek'], 
        data=[[neighborhood,grade_prior, score_prior, violations_prior, critical_violations_prior,persons_per_acre,female_to_male,adults_to_minor, inspection_date_month,inspection_date_dayofweek]]
    )
      
    y_pred = pipeline.predict(df)[0]
    if y_pred == 'pass':
        y_pred_proba = pipeline.predict_proba(df)[0][0]
        return f'{y_pred_proba*100:.0f}% chance of a {y_pred}'
    else:
        y_pred_proba = pipeline.predict_proba(df)[0][1]
        return f'{y_pred_proba*100:.0f}% chance of a {y_pred}'

# @app.callback(
#     Output(component_id='my-daq-gauge', component_property='value'),
#     [Input(component_id='slider1', component_property='value')]
# )
# def update_output_div(input_value):
#     # return 'You\'ve entered "{}"'.format(input_value)
#     return input_value

