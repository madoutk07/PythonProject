import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from moteurRecherche import RechercherAuteur, RechercherSource, RechercherTfIdf
from Model.Corpus import Corpus

corpus = Corpus.load("Data/corpus.pkl")


# Exemple de données
data = [
    {'Mot_clé': 'Python', 'Auteur': 'Auteur1', 'Date': '2024-01-01', 'Source': 'Reddit'},
    {'Mot_clé': 'Dash', 'Auteur': 'Auteur2', 'Date': '2025-01-02', 'Source': 'Arxiv'},
    {'Mot_clé': 'Data Science', 'Auteur': 'Auteur3', 'Date': '2026-01-03', 'Source': 'Arxiv'}
]

df = pd.DataFrame(data)

app = dash.Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#f2f2f2', 'padding': '50px', 'height': '100vh'}, children=[
    html.H1("Bienvenue", style={'textAlign': 'center', 'color': '#333', 'marginBottom': 20}),

# Formulaire de recherche
html.Div([
    html.Label("Mot_clé:", style={'color': '#333', 'marginBottom': '10px', 'padding': '10px', 'fontSize': 15}),
    dcc.Input(id='keyword_input', type='text', placeholder='Entrez le mot-clé', style={'width': '75%', 'marginBottom': 20, 'padding': '10px', 'fontSize': 14}),

    html.Label("Auteur:", style={'color': '#333', 'marginBottom': '10px', 'padding': '10px', 'fontSize': 15}),
    dcc.Input(id='author_input', type='text', placeholder="Entrez le nom de l'auteur", style={'width': '75%', 'marginBottom': 20, 'padding': '10px', 'fontSize': 14}),

    html.Label("Source:", style={'color': '#333', 'marginBottom': '10px', 'padding': '10px', 'fontSize': 15}),
    dcc.Dropdown(
        id='genre_dropdown',
        options=[
            {'label': 'Reddit', 'value': 'Reddit'},
            {'label': 'Arxiv', 'value': 'Arxiv'}
        ],
        placeholder="Sélectionnez le genre de l'article",
        style={'color': '#333', 'marginBottom': '10px', 'padding': '10px','width':'75%' ,'fontSize': 15}
    ),

    html.Button('Rechercher', id='search_button', n_clicks=0, style={'backgroundColor': '#4CAF50', 'color': 'white', 'padding': '10px 20px', 'fontSize': 16, 'margin':'10px'}),
], style={'margin': '5px', 'borderRadius': '10px', 'boxShadow': '0px 0px 10px 0px rgba(0,0,0,0.1)', 'display': 'flex', 'width': '100%', 'verticalAlign': 'top', 'flexDirection': 'row', 'alignItems': 'center'}),


    # Résultats de la recherche
    html.Div(id='search_results', style={'marginTop': 20, 'fontSize': 18, 'color': '#333', 'display': 'none'}),

    # Message d'erreur
    html.Div(id='error_message', style={'color': 'red', 'marginTop': '10px'}),
])


@app.callback(
    [Output('search_results', 'children'),
     Output('search_results', 'style'),
     Output('error_message', 'children')],
    [Input('search_button', 'n_clicks')],
    [State('author_input', 'value'),
     State('keyword_input', 'value'),
     State('genre_dropdown', 'value')]
)
def update_search_results(n_clicks, author_query, keyword_query, genre_query):
    if n_clicks == 0:
        raise PreventUpdate

    if not any([author_query, keyword_query, genre_query]):
        error_message = "Veuillez entrer au moins un critère de recherche."
        return [], {'display': 'none'}, error_message

    if (keyword_query):
        filtered_results = RechercherTfIdf(keyword_query, corpus)

    if (author_query):
        filtered_results = RechercherAuteur(keyword_query, corpus)
    if (genre_query):
        if (genre_query == "Reddit"):
            genre_query = "Reddit"
        if (genre_query == "Arxiv"):
            genre_query = "Arxiv"
        filtered_results = RechercherSource(genre_query, corpus)

    # print(filtered_results)
    # filtered_results = [
    #     result for result in data
    #     if (str(author_query) in result['Auteur']) or
    #        (keyword_query in result['Mot_clé']) or
    #        (genre_query == result['Source'])
    # ]

    if not filtered_results:
        error_message = "Aucun résultat trouvé pour les critères de recherche spécifiés."
        return [], {'display': 'none'}, error_message

    search_results = [
        html.Div([
            html.H4(result["titre"], style={'margin-bottom': '5px'}),
            html.P(f"{result['texte']}"),
            html.P(f"Auteur: {result['auteur']} \t| Source: {result['source']}"),
            html.P(f"Lien: {result['url']}", style={'color': '#1a0dab'})
        ], style={'background-color': 'white', 'border': '1px solid #ddd', 'padding': '10px', 'marginBottom': '10px'})
        for result in filtered_results
    ]

    style = {'marginTop': 20, 'fontSize': 18, 'color': '#333', 'display': 'block'}
    error_message = ""

    return search_results, style, error_message


if __name__ == '__main__':
    app.run_server(debug=True)
