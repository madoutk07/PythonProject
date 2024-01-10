

class Document:
    """
    Classe représentant un document.

    Attributes:
        titre (str): Le titre du document.
        auteur (str): L'auteur du document.
        date (str): La date du document.
        url (str): L'URL du document.
        texte (str): Le texte du document.
    """

    def __init__(self, titre="", auteur="", date="", url="", texte="" ):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

    def __repr__(self):
        """
        Renvoie une représentation du document.

        Returns:
            str: La représentation du document.
        """
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\tType : {self.getType()}"

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant le document.

        Returns:
            str: La représentation du document.
        """
        return f"{self.titre}, par {self.auteur}"

    def getType(self):
        """
        Renvoie le type du document.

        Returns:
            str: Le type du document.
        """
        pass


class RedditDocument(Document):
    """
    Classe représentant un document Reddit.

    Attributes:
        nbcommentaires (int): Le nombre de commentaires du document Reddit.
    """

    def __init__(self, titre="", auteur="", date="", url="", texte="", nbcommentaires=0):
        super().__init__(titre, auteur, date, url, texte)
        self._nbcommentaires = nbcommentaires

    def getNbcommentaires(self):
        """
        Renvoie le nombre de commentaires du document Reddit.

        Returns:
            int: Le nombre de commentaires du document Reddit.
        """
        return self._nbcommentaires

    def setNbcommentaires(self, nbcommentaires):
        """
        Modifie le nombre de commentaires du document Reddit.

        Args:
            nbcommentaires (int): Le nouveau nombre de commentaires.
        """
        self._nbcommentaires = nbcommentaires

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant le document Reddit.

        Returns:
            str: La représentation du document Reddit.
        """
        return super().__str__() + f"\tNombre de commentaires : {self.getNbcommentaires()}"
        # return super().__str__() + f"\tNombre de commentaires  "

    def getType(self):
        """
        Renvoie le type du document.

        Returns:
            str: Le type du document.
        """
        return "Reddit"



class ArxivDocument(Document):
    """
    Classe représentant un document Arxiv.

    Attributes:
        co_auteurs (list): La liste des co-auteurs du document Arxiv.
    """

    def __init__(self, titre="", auteur="", date="", url="", texte="", co_auteurs=[]):
        self._co_auteurs = co_auteurs
        super().__init__(titre, auteur, date, url, texte)

    def getType(self):
        """
        Renvoie le type du document.

        Returns:
            str: Le type du document.
        """
        return "Arxiv"

    def getCo_auteurs(self):
        """
        Renvoie la liste des co-auteurs du document Arxiv.

        Returns:
            list: La liste des co-auteurs du document Arxiv.
        """
        return self._co_auteurs

    def setCo_auteurs(self, co_auteurs):
        """
        Modifie la liste des co-auteurs du document Arxiv.

        Args:
            co_auteurs (list): La nouvelle liste des co-auteurs.
        """
        self._co_auteurs = co_auteurs

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant le document Arxiv.

        Returns:
            str: La représentation du document Arxiv.
        """
        return super().__str__() + f"\tCo-auteurs : {self.getCo_auteurs()}"
        # return super().__str__()
