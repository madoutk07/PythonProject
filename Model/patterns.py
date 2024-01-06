from Model.Classes import ArxivDocument, RedditDocument

def singleton(cls):
    """
   design pattern Singleton.
    Args:
        cls: La classe à décorer.
    Returns:
        La classe décorée.
    Raises:
        Exception: Si une instance de la classe existe déjà.
    """
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            try:
                instances[cls] = cls(*args, **kwargs)
                return instances[cls]
            except Exception:
                raise("bug")
        else:
            raise Exception("une instance de la classe existe déjà")
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


