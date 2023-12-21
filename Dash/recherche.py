import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    style={'textAlign': 'center', 'margin': '50px'},
    children=[
        html.H1("Search Interface", style={'color': 'blue'}),
        dcc.Input(
            id="search-input",
            type="text",
            placeholder="Enter your search query",
            style={'margin': '10px'}
        ),
        html.Button("Search", id="search-button"),
        html.Div(id="search-results"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
