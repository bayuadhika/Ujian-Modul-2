import plotly
import plotly.graph_objects  as go
import plotly.express as px
from cleaning_data import IndiaClean
import json

def count_type1():
    df = IndiaClean()
    
    fig = go.Figure([
        go.Bar(x=df['Industry Vertical'] , y= df['Amount in USD'])
    ])

    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    

def dist_total():
    df= IndiaClean()
    fig = px.box(df, x='City  Location' , y='Amount in USD')
    
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json