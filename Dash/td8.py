import pandas as pd
import dash
from dash import dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px


#----- CHARGEMENT DES DONNÉES
data = pd.read_excel("./Data/velib.xlsx")
df = pd.DataFrame(data)
print("ok ça fonctionne")

ok = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#ok = dash.Dash(__name__)
# App layout
# ok.layout = html.Div([
#     html.Div(children='App with Data and a Graph'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10),
#     dcc.Graph(figure=px.histogram(df, x='Unnamed: 0', y='V1', histfunc='avg'))
# ])

# @callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
# def update_graphs(active_cell):
#     return str(active_cell) if active_cell else "Click the table"


ok.layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
    dbc.Alert(id='tbl_out'),
    html.Div([
    html.Div(children='App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='Unnamed: 0', y='V1', histfunc='avg'))
])
])

@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"


#ok.layout = dash_table.DataTable(df.to_dict('records'),[{"name":i, "id":i} for i in df.columns])
#ok.layout = dbc.Container(
    #dbc.Label('Click a cell in the table:'),dash_table.DataTable(df.to_dict('records'),  dbc.Alert(id='tbl_out'),


     #         style_cell_conditional=[
      #  {
       #     'if': {'column_id': c},
        #    'textAlign': 'left'
        #} for c in ['Date', 'Region']
    #],
    #style_header={
    #    'backgroundColor': 'green',
     #   'fontWeight': 'bold'
    #},

    #style_as_list_view=True,

#))

#@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
#def update_graphs(active_cell):
   # return str(active_cell) if active_cell else "Click the table"


if __name__ == '__main__':
    ok.run(debug=True)





