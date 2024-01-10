import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Exemple de données
data = [
    {'Mot_clé': 'Python', 'Auteur': 'Auteur1', 'Date': '2024-01-01', 'Source': 'Reddit'},
    {'Mot_clé': 'Dash', 'Auteur': 'Auteur2', 'Date': '2025-01-02', 'Source': 'Arxiv'},
    {'Mot_clé': 'Data Science', 'Auteur': 'Auteur3', 'Date': '2026-01-03', 'Source': 'Arxiv'}
]

df = pd.DataFrame(data)

app = dash.Dash(__name__)


app.layout = html.Div(style={'backgroundColor': '#f2f2f2', 'padding': '50px', 'height': '100vh'}, children=[
    html.H1("Corpus", style={'textAlign': 'center', 'color': '#333', 'marginBottom': 20}),
    
    # Formulaire de recherche
    html.Div([
        html.Label("Mot_clé:", style={'color': '#333', 'fontSize': 16}),
        dcc.Input(id='keyword_input', type='text', placeholder='Entrez le mot-clé', style={'width': '95%', 'marginBottom': 20, 'padding': '10px', 'fontSize': 14}),
        
        html.Label("Auteur:", style={'color': '#333', 'fontSize': 16}),
        dcc.Input(id='author_input', type='text', placeholder="Entrez le nom de l'auteur", style={'width': '95%', 'marginBottom': 20, 'padding': '10px', 'fontSize': 14}),
      
        html.Label("Source:", style={'color': '#333', 'fontSize': 16}),
        dcc.Dropdown(
            id='genre_dropdown',
            options=[
                {'label': 'Reddit', 'value': 'Reddit'},
                {'label': 'Arxiv', 'value': 'Arxiv'}
            ],
            placeholder="Sélectionnez le genre de l'article",
            style={'width': '95%', 'marginBottom': 20, 'padding': '10px', 'fontSize': 14}
        ),
        
        html.Button('Rechercher', id='search_button', n_clicks=0, style={'backgroundColor': '#4CAF50', 'color': 'white', 'padding': '10px 20px', 'fontSize': 16}),
    ], style={'maxWidth': '600px', 'margin': 'auto', 'borderRadius': '10px', 'boxShadow': '0px 0px 10px 0px rgba(0,0,0,0.1)'}),

    # Résultats de la recherche
    html.Div(id='search_results', style={'marginTop': 20, 'fontSize': 18, 'color': '#333'}),
])

# Callback pour mettre à jour les résultats de la recherche
@app.callback(
    Output('search_results', 'children'),
    [Input('search_button', 'n_clicks')],
    [State('author_input', 'value'),
     State('keyword_input', 'value'),
     State('genre_dropdown', 'value')]
)
def update_search_results(n_clicks, author_query, keyword_query, genre_query):
    if n_clicks == 0:
        raise PreventUpdate

    filtered_results = [
        result for result in data
        if (str(author_query) in result['Auteur']) or
           (keyword_query in result['Mot_clé']) or
           (genre_query == result['Source'])
    ]

    search_results = [html.P(f"Mot_clé: {result['Mot_clé']} | Auteur : {result['Auteur']} | Source: {result['Source']}") for result in filtered_results]

    return search_results

if __name__ == '__main__':
    app.run_server(debug=True)
