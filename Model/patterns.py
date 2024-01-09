from Model.Document import ArxivDocument, RedditDocument


def singleton(cls):
    """
    Décorateur pour créer une classe singleton.

    Args:
        cls: La classe à décorer.

    Returns:
        La classe décorée en tant que singleton.
    """
    instances = [None]
    def wrapper(*args, **kwargs):
        if instances[0] is None:
            instances[0] = cls(*args, **kwargs)
        return instances[0]
    return wrapper


class DocumentGenerator:
    """
    Génère des documents en fonction des paramètres fournis.
    """

    @staticmethod
    def factory(titre, auteur, date, url, texte ,nbcommentaires = None, co_auteurs = None):
        """
        Méthode statique qui crée une instance de la classe ArxivDocument ou RedditDocument en fonction des paramètres fournis.

        Args:
            titre : Le titre du document.
            auteur : L'auteur du document.
            date : La date du document.
            url : L'URL du document.
            texte : Le texte du document.
            nbcommentaires : Le nombre de commentaires (uniquement pour RedditDocument).
            co_auteurs : La liste des co-auteurs (uniquement pour ArxivDocument). Defaults to None.

        Returns:
            ArxivDocument or RedditDocument: Une instance de la classe ArxivDocument ou RedditDocument.

        Raises:
            AssertionError: Si aucun paramètre optionnel n'est fourni.
        """
        if nbcommentaires is not None:
            return RedditDocument(titre, auteur, date, url, texte, nbcommentaires)
        if co_auteurs is not None:
            return ArxivDocument(titre, auteur, date, url, texte, co_auteurs)
        assert 0, "erreur "+type


