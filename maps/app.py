from flask import Flask, render_template
import plotly
import json
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import boto3
from dash.dependencies import Input, Output
app = Flask(__name__)


@app.route('/')
def index():
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='output_container_two', component_property='children'),
     Output(component_id='map', component_property='figure')],
    [Input(component_id='my_slider', component_property='value'),
     Input(component_id='dropdown', component_property='value')]
    bar = create_plot()
    return render_template('index.html', plot=bar)

def load_data():
    client = boto3.client('s3')
    ### Data: Use old ipynb from ecl
    county_geo = pd.read_csv('tl_2017_us_county.csv')
    county_geo = county_geo[['GEOID']]
    county_geo_org = county_geo.sort_values(by='GEOID')
    county_geo_org['GEOID'] = county_geo_org['GEOID'].astype('str')
    county_geo_org = county_geo_org.drop([1248, 1460, 81])
    path = "s3://ecodatalab/data/"
    ten = pd.read_csv( path + 'counties5year2010clean.csv'); ten.insert(0, 'year', 2010)
    eleven = pd.read_csv(path + 'counties5year2011clean.csv'); eleven.insert(0, 'year', 2011)
    twelve = pd.read_csv(path + 'counties5year2012clean.csv'); twelve.insert(0, 'year', 2012)
    thirteen = pd.read_csv(path + 'counties5year2013clean.csv'); thirteen.insert(0, 'year', 2013)
    fourteen = pd.read_csv(path + 'counties5year2014clean.csv'); fourteen.insert(0, 'year', 2014)
    fifteen = pd.read_csv(path + 'counties5year2015clean.csv'); fifteen.insert(0, 'year', 2015)
    sixteen = pd.read_csv(path + 'counties5year2016clean.csv'); sixteen.insert(0, 'year', 2016)
    seventeen = pd.read_csv(path + 'counties5year2017clean.csv'); seventeen.insert(0, 'year', 2017)
    frames = [ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen]
    # newdf = pd.read_csv(path + 'carbon_data_county.csv')
    newdf = pd.concat(frames)
    newdf = newdf.rename(columns={"year": "YEAR", "Geo_NAME":"County Name", "DEGREE":"DEGREE", "MEDINCOME":"MEDINCOME", "AVGINCOME":"AVGINCOME", "OWN":"OWN", "SIZE":"SIZE", "ROOMS":"ROOMS", "VEHICLES":"VEHICLES", "Geo_FIPS":"GEOID"})
    newdf['GEOID'] = newdf['GEOID'].astype(str)
    finaldf = county_geo_org.merge(newdf, on=['GEOID'])
    finaldf['GEOID'] = finaldf['GEOID'].replace("46102", "46113")
    finaldf['GEOID'] = finaldf['GEOID'].replace("2158", "2270")
    return finaldf

def create_plot():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__ == '__main__':
    app.run()