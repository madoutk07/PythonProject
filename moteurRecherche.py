import Model.Corpus as Corpus
from difflib import SequenceMatcher

def comparerAuteur(a, b):
    """
    Compare deux auteurs et retourne le ratio de similarité entre eux.

    Args:
        a (str): Le premier auteur.
        b (str): Le deuxième auteur.

    Returns:
        float: Le ratio de similarité entre les deux auteurs.
    """
    return SequenceMatcher(None, a, b).ratio()

def FaireVocabulaire(phrase):
    """
    Crée un vocabulaire à partir d'une phrase donnée.

    Args:
        phrase (str): La phrase à partir de laquelle créer le vocabulaire.

    Returns:
        set: Le vocabulaire créé.
    """
    vocab = set()
    phrase = Corpus.nettoyer_texte(phrase)
    phrase = phrase.split(' ')
    phrase = [mot for mot in phrase if mot != '']
    vocab.update(phrase)
    return vocab

def RechercherTfIdf(phrase, corpus):
    """
    Recherche les documents les plus similaires à une phrase donnée en utilisant la méthode TF-IDF.

    Args:
        phrase (str): La phrase à rechercher.
        corpus (Corpus): L'objet Corpus contenant les documents.

    Returns:
        list: Une liste de dictionnaires contenant les informations des documents similaires.
    """
    vocab = FaireVocabulaire(phrase)
    similarite = corpus.calculer_similarite_TFxIDF(vocab)
    ListeDoc = []
    for id, score in similarite:
        dic = {
            "titre": corpus.id2doc[id].titre,
            "auteur": corpus.id2doc[id].auteur,
            "date": corpus.id2doc[id].date,
            "url": corpus.id2doc[id].url,
            "texte": corpus.id2doc[id].texte[:500],
            "source": corpus.id2doc[id].getType(),
            "score": score
        }
        ListeDoc.append(dic)
    return ListeDoc

def RechercherTf(phrase, corpus):
    """
    Recherche les documents les plus similaires à une phrase donnée en utilisant la méthode TF.

    Args:
        phrase (str): La phrase à rechercher.
        corpus (Corpus): L'objet Corpus contenant les documents.

    Returns:
        list: Une liste de dictionnaires contenant les informations des documents similaires.
    """
    vocab = FaireVocabulaire(phrase)
    similarite = corpus.calculer_similarite_TF(vocab)
    ListeDoc = []
    for id, score in similarite:
        dic = {
            "titre": corpus.id2doc[id].titre,
            "auteur": corpus.id2doc[id].auteur,
            "date": corpus.id2doc[id].date,
            "url": corpus.id2doc[id].url,
            "texte": corpus.id2doc[id].texte[:500],
            "source": corpus.id2doc[id].getType(),
            "score": score
        }
        ListeDoc.append(dic)
    return ListeDoc

def RechercherAuteur(NomAuteur, corpus):
    """
    Recherche les documents écrits par un auteur donné.

    Args:
        NomAuteur (str): Le nom de l'auteur à rechercher.
        corpus (Corpus): L'objet Corpus contenant les documents.

    Returns:
        list: Une liste de dictionnaires contenant les informations des documents écrits par l'auteur.
    """
    ListeDoc = []
    for auteur in corpus.authors.values():
        temp = comparerAuteur(auteur.name, NomAuteur)
        if temp > 0.5:
            for titre in auteur.production:
                for elemnt in corpus.id2doc.values():
                    if elemnt.titre == titre:
                        dic = {
                            "titre": elemnt.titre,
                            "auteur": elemnt.auteur,
                            "date": elemnt.date,
                            "url": elemnt.url,
                            "texte": elemnt.texte[:500],
                            "source": elemnt.getType(),
                            "score": temp

                        }
                        ListeDoc.append(dic)
                        break
    return ListeDoc

def RechercherSource(source, corpus):
        ListeDoc = []
        for cle, elemnt in corpus.id2doc.items():
            if elemnt.getType() == source:
                dic = {
                            "titre": elemnt.titre,
                            "auteur": elemnt.auteur,
                            "date": elemnt.date,
                            "url": elemnt.url,
                            "texte": elemnt.texte[:500],
                            "source": elemnt.getType()

                }
                ListeDoc.append(dic)

        return ListeDoc