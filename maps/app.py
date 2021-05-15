### Imports and Initializations
from numpy import place
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
import plotly.express as px
import plotly.graph_objects as go
import boto3
import dash
import json
from urllib.request import urlopen
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash_extensions.callback import CallbackCache
from flask_caching import Cache
from flask_caching.backends import FileSystemCache
import warnings
warnings.filterwarnings('ignore')
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
cc = CallbackCache()

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
server = app.server
TIMEOUT = 60
@cache.memoize(timeout=TIMEOUT)
def load_counties():
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
        return counties

@cache.memoize(timeout=TIMEOUT)
def load_data(year):
    client = boto3.client('s3')
    
    ### Data: Use old ipynb from ecl
    county_geo = pd.read_csv('tl_2017_us_county.csv')
    county_geo = county_geo[['GEOID']]
    county_geo_org = county_geo.sort_values(by='GEOID')
    county_geo_org['GEOID'] = county_geo_org['GEOID'].astype('str')

    county_geo_org = county_geo_org.drop([1248, 1460, 81])


    path = "s3://ecodatalab/data/"
    path_name = "counties5year" + str(year) + "clean.csv"
    df = pd.read_csv(path+path_name)

    newdf = df.rename(columns={"year": "YEAR", "Geo_NAME":"County Name", "DEGREE":"DEGREE", "MEDINCOME":"MEDINCOME", "AVGINCOME":"AVGINCOME", "OWN":"OWN", "SIZE":"SIZE", "ROOMS":"ROOMS", "VEHICLES":"VEHICLES", "TOTAL":"TOTAL", "Geo_FIPS":"GEOID"})
    newdf['GEOID'] = newdf['GEOID'].astype(str)

    finaldf = county_geo_org.merge(newdf, on=['GEOID'])

    finaldf['GEOID'] = finaldf['GEOID'].replace("46102", "46113")

    finaldf['GEOID'] = finaldf['GEOID'].replace("2158", "2270")
    return finaldf

@cache.memoize(timeout=TIMEOUT)
def load_placeholder():
    client = boto3.client('s3')
    

    ### Data: Use old ipynb from ecl
    county_geo = pd.read_csv('tl_2017_us_county.csv')
    county_geo = county_geo[['GEOID']]
    county_geo_org = county_geo.sort_values(by='GEOID')
    county_geo_org['GEOID'] = county_geo_org['GEOID'].astype('str')

    county_geo_org = county_geo_org.drop([1248, 1460, 81])


    path = "s3://ecodatalab/data/"
    path_name = "counties5year" + str(2010) + "clean.csv"
    df = pd.read_csv(path+path_name)
    # ten = pd.read_csv( path + 'counties5year2010clean.csv'); ten.insert(0, 'year', 2010)
    # eleven = pd.read_csv(path + 'counties5year2011clean.csv'); eleven.insert(0, 'year', 2011)
    # twelve = pd.read_csv(path + 'counties5year2012clean.csv'); twelve.insert(0, 'year', 2012)
    # thirteen = pd.read_csv(path + 'counties5year2013clean.csv'); thirteen.insert(0, 'year', 2013)
    # fourteen = pd.read_csv(path + 'counties5year2014clean.csv'); fourteen.insert(0, 'year', 2014)
    # fifteen = pd.read_csv(path + 'counties5year2015clean.csv'); fifteen.insert(0, 'year', 2015)
    # sixteen = pd.read_csv(path + 'counties5year2016clean.csv'); sixteen.insert(0, 'year', 2016)
    # seventeen = pd.read_csv(path + 'counties5year2017clean.csv'); seventeen.insert(0, 'year', 2017)
    # frames = [ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen]
    # # newdf = pd.read_csv(path + 'carbon_data_county.csv')



    # newdf = pd.concat(frames)

    newdf = df.rename(columns={"year": "YEAR", "Geo_NAME":"County Name", "DEGREE":"DEGREE", "MEDINCOME":"MEDINCOME", "AVGINCOME":"AVGINCOME", "OWN":"OWN", "SIZE":"SIZE", "ROOMS":"ROOMS", "VEHICLES":"VEHICLES", "TOTAL":"TOTAL", "Geo_FIPS":"GEOID"})
    newdf['GEOID'] = newdf['GEOID'].astype(str)

    finaldf = county_geo_org.merge(newdf, on=['GEOID'])

    finaldf['GEOID'] = finaldf['GEOID'].replace("46102", "46113")

    finaldf['GEOID'] = finaldf['GEOID'].replace("2158", "2270")
    return finaldf

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#D6E7FF",
}
# padding for the page content
CONTENT_STYLE = {
    "margin-left": "8.5rem",
    "margin-right": "4rem",
    "width":"160vh",
    "margin-top":"20px"
    # "padding": "2rem 1rem",
}
SLIDER_STYLE = {
    "margin-left": "16rem",
    # "margin-right": "2rem",
    # "padding-left": "9rem",
    "margin-top": "50px",
    "width":"160vh"
}
MAP_STYLE = {
    "margin-left": "12rem",
    # "margin-right": "4rem",
    # "padding-left": "2rem",
    "width":"170vh",
    "height":"100vh",
    "padding-top":"-100px",
    "margin-top":"-20px"
}
sidebar = html.Div(
    [
        html.H2("EcoDataLab", className="display-6", style={"font-family":"Candara", "text-align":"center"}),
        html.Hr(),
        # html.P(
        #     "Improving the carbon footprint one map at a time", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact", style={"font-family":"Candara"}),
                dbc.NavLink("Change Over Time", href="/delta", active="exact", style={"font-family":"Candara"}),
                # dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True
        ),
        dcc.Markdown(children=
            '''
                __**Glossary**__\n
                **Total Carbon Footprint**: Carbon Footprint estimation based on consumer expenditure and consumption\n
                **Degree**: Average number of degrees attained\n
                **Rooms per Household**: Average number of rooms per household\n
                **Home Ownership**: Average number of homes owned\n
                **Vehicle Ownership**: Average number of vehicles owned\n
            ''',
            style={"font-size":"12px", "margin-top":"40px"}
        ),
        html.H6("Created by Viren Khandal", className="display-9", style={"font-family":"Candara", "font-size":"10px", "text-align":"center", "margin-left":"auto", "margin-right":"auto", "left":"0", "right":"0", "position":"absolute", "bottom":"0"})
    ],
    style=SIDEBAR_STYLE
)

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(style=SLIDER_STYLE, children=[
    dcc.Slider(
        id='my_slider',
        min=2010,
        max=2017,
        step=1,
        value=2014,
        marks={
        2010: '2010',
        2011: '2011',
        2012: '2012',
        2013: '2013',
        2014: '2014',
        2015: '2015',
        2016: '2016',
        2017: '2017'
        },
        included=False
    )]),

    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Total Carbon Footprint', 'value': 'TOTAL'},
            {'label': 'Degree', 'value': 'DEGREE'},
            # {'label': 'Average Income', 'value': 'AVGINCOME'},
            # {'label': 'Median Income', 'value': 'MEDINCOME'},
            {'label': 'Rooms per Household', 'value': 'ROOMS'},
            {'label': 'Home Ownership', 'value': 'OWN'},
            {'label': 'Vehicle Ownership', 'value': 'VEHICLES'}
        ],
        value='TOTAL',
        placeholder="Select a variable to display on the map",
        style=CONTENT_STYLE
    ),

    # html.Div(id='output_container', children=[], style=CONTENT_STYLE),
    # html.Div(id='output_container_two', children=[], style=CONTENT_STYLE),
    html.Br(),

    dcc.Loading(
            id="loading-1",
            type="cube",
            color="#3FA155",
            # fullscreen=True,
            children=dcc.Graph(id='map', figure={}, style=MAP_STYLE),
    ),
    sidebar
])


@app.callback(
    Output("map", "figure"),
    [Input("url", "pathname"),
     Input(component_id='my_slider', component_property='value'),
     Input(component_id='dropdown', component_property='value')]
    )
@cache.cached(timeout=50)
def render_page_content(pathname, my_slider, dropdown):
    year = my_slider
    variable = dropdown
    finaldf = load_data(year)
    counties = load_counties()
    if pathname == "/":
        finaldf['GEOID'] = finaldf['GEOID'].str.zfill(5)
        min_value = finaldf[variable].min()
        max_value = finaldf[variable].max()
        fig = px.choropleth(
            data_frame=finaldf,
            geojson=counties,
            locations=finaldf["GEOID"],
            scope="usa",
            color=variable,
            hover_data=['County Name', variable],
            color_continuous_scale="temps",
            labels={str(variable): variable},
            range_color = [min_value, max_value]
        )
        fig.update_layout(geo=dict(bgcolor= 'rgba(189, 222, 240, 1)', lakecolor='#BDDEF0'))
        fig.update_traces(marker_line_width=0)
        fig.update_geos(visible=False, resolution=110, scope="usa")   
        # print(fig)
        return fig
    elif pathname == "/delta":
        placeholder = load_placeholder()
        finaldf[variable] = finaldf[variable].values / placeholder[variable].values
        finaldf['GEOID'] = finaldf['GEOID'].str.zfill(5)
        min_value = finaldf[variable].min()
        max_value = finaldf[variable].max()
        fig = px.choropleth(
            data_frame=finaldf,
            geojson=counties,
            locations=finaldf["GEOID"],
            scope="usa",
            color=variable,
            hover_data=['County Name', variable],
            color_continuous_scale="RdYlGn",
            labels={str(variable): variable},
            range_color = [min_value, max_value]
        )
        fig.update_layout(geo=dict(bgcolor= 'rgba(189, 222, 240, 1)', lakecolor='#BDDEF0'))
        fig.update_traces(marker_line_width=0)
        fig.update_geos(
            visible=False, resolution=110, scope="usa"
        )   
        return fig
    # elif pathname == "/page-2":
    #     return [
    #             html.H1('High School in Iran',
    #                     style={'textAlign':'center'}),
    #             dcc.Graph(id='bargraph',
    #                      figure=px.bar(df, barmode='group', x='Years',
    #                      y=['Girls High School', 'Boys High School']))
    #             ]
    # If the user tries to reach a different page, return a 404 message
    # return dbc.Jumbotron(
    #     [
    #         html.H1("404: Not found", className="text-danger"),
    #         html.Hr(),
    #         html.P(f"The pathname {pathname} was not recognised..."),
    #     ]
    # )

cc.register(app)
### Run
if __name__ == '__main__':
    app.run_server(debug=True)