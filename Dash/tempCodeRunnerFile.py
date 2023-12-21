ok.layout = html.Div([
#     html.Div(children='App with Data and a Graph'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10),
#     dcc.Graph(figure=px.histogram(df, x='Unnamed: 0', y='V1', histfunc='avg'))
# ])

# @callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
# def update_graphs(active_cell):
#     return str(active_cell) if active_cell else "Click the table"