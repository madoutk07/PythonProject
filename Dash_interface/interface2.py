import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
from dash.exceptions import PreventUpdate

# Exemple de données
data = [
    {'Mot_clé': 'Python', 'Auteur': 'Auteur1', 'Date': '2024-01-01', 'Source': 'Reddit'},
    {'Mot_clé': 'Dash', 'Auteur': 'Auteur2', 'Date': '2025-01-02', 'Source': 'Arxiv'},
    {'Mot_clé': 'Data Science', 'Auteur': 'Auteur3', 'Date': '2026-01-03', 'Source': 'Arxiv'}
]

df = pd.DataFrame(data)

app = dash.Dash(__name__)

# Layout principal avec le formulaire de recherche
app.layout = html.Div(style={'backgroundColor': '#f2f2f2', 'padding': '10px', 'height': '100vh'}, children=[
    html.Div([
        html.H1("Corpus", style={'textAlign': 'center', 'color': '#333', 'marginBottom': 20}),

      html.Div([
    html.Label("Mot_clé:", style={'display': 'inline-block'}),

    dcc.Input(id='keyword_input', type='text', placeholder='Entrez le mot-clé', style={'display': 'inline-block'}),

    html.Label("Auteur:", style={'display': 'inline-block'}),

    dcc.Input(id='author_input', type='text', placeholder="Entrez le nom de l'auteur", style={'display': 'inline-block'}),

    html.Label("Source:", style={'display': 'inline-block'}),

    dcc.Dropdown(
        id='genre_dropdown',
        options=[
            {'label': 'Reddit', 'value': 'Reddit'},
            {'label': 'Arxiv', 'value': 'Arxiv'}
        ],
        placeholder="Sélectionnez le genre de l'article",
        style={'display': 'inline-block'}
    ),


],),






        html.Div(id='search_results', style={'marginTop': 20, 'fontSize': 18, 'color': '#333'}),

    ],)
])

search_results = []  # Variable pour stocker les résultats de la recherche

# Callback pour mettre à jour les résultats de la recherche
@app.callback(
    Output('search_results', 'children'),
    [Input('search_button', 'n_clicks')],
    [State('author_input', 'value'),
     State('keyword_input', 'value'),
     State('genre_dropdown', 'value')]
)
def update_search_results(n_clicks, author_query, keyword_query, genre_query):
    global search_results

    # if n_clicks == 0:
    #     raise PreventUpdate  # Aucune mise à jour avant le clic sur le bouton

    filtered_results = [
        result for result in data
        if (str(author_query) in result['Auteur']) and
           (keyword_query in result['Mot_clé']) and
           (genre_query == result['Source'])
    ]

    search_results = filtered_results

    return [html.P(f"Auteur: {result['Auteur']} | Mot_clé: {result['Mot_clé']} | Source: {result['Source']}") for result in search_results]
print("ok")

# Fonction pour générer le layout des résultats de recherche
# def generate_search_results_layout(results):
#     return html.Div([
#         html.H1("Résultats de la Recherche", style={'textAlign': 'center'}),
#         html.Div([generate_result_link(result) for result in results])
#     ])
print ("ok2")
# def initial_layout():
#     if not search_results:
#         return app.layout
#     else:
#         return generate_search_results_layout(search_results)


def generate_result_link(result):
    return dcc.Link(
        html.Div([
            html.H3(result['Mot_clé'], style={'margin-bottom': '5px'}),
            html.P(f"Auteur: {result['Auteur']} | Date: {result['Date']} | Source: {result['Source']}")
        ]),
        href=f"/result/{result['Mot_clé']}",
        style={'text-decoration': 'none', 'color': 'black'}
    )
print ("ok3")
# app.layout = initial_layout

if __name__ == '__main__':
    app.run_server(debug=True)
