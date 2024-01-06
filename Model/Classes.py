# Correction de G. Poux-Médard, 2021-2022

# =============== 2.1 : La classe Document ===============

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


# =============== 2.4 : La classe Author ===============

class Author:
    """
    Classe représentant un auteur.

    Attributes:
        name (str): Le nom de l'auteur.
        ndoc (int): Le nombre de documents produits par l'auteur.
        production (list): La liste des productions de l'auteur.
    """

    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = []

    def add(self, production):
        """
        Ajoute une production à l'auteur.

        Args:
            production: La production à ajouter.
        """
        self.ndoc += 1
        self.production.append(production)

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant l'auteur.

        Returns:
            str: La représentation de l'auteur.
        """
        return f"Auteur : {self.name}\t# productions : {self.ndoc}"


# =============== TD5.1 : rEDDITdOCUMENT ===============

class RedditDocument(Document):
    """
    Classe représentant un document Reddit.

    Attributes:
        nbcommentaires (int): Le nombre de commentaires du document Reddit.
    """

    def __init__(self, titre="", auteur="", date="", url="", texte="", nbcommentaires=0):
        super().__init__(titre, auteur, date, url, texte)
        self.nbcommentaires = nbcommentaires

    def getNbcommentaires(self):
        """
        Renvoie le nombre de commentaires du document Reddit.

        Returns:
            int: Le nombre de commentaires du document Reddit.
        """
        return self.nbcommentaires

    def setNbcommentaires(self, nbcommentaires):
        """
        Modifie le nombre de commentaires du document Reddit.

        Args:
            nbcommentaires (int): Le nouveau nombre de commentaires.
        """
        self.nbcommentaires = nbcommentaires

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant le document Reddit.

        Returns:
            str: La représentation du document Reddit.
        """
        return super().__str__() + f"\tNombre de commentaires : {self.nbcommentaires}"

    def getType(self):
        """
        Renvoie le type du document.

        Returns:
            str: Le type du document.
        """
        return "Reddit"


# =============== TD5. 2 : ArxivDocument ===============

class ArxivDocument(Document):
    """
    Classe représentant un document Arxiv.

    Attributes:
        co_auteurs (list): La liste des co-auteurs du document Arxiv.
    """

    def __init__(self, titre="", auteur="", date="", url="", texte="", co_auteurs=[]):
        self.co_auteurs = co_auteurs
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
        return self.co_auteurs

    def setCo_auteurs(self, co_auteurs):
        """
        Modifie la liste des co-auteurs du document Arxiv.

        Args:
            co_auteurs (list): La nouvelle liste des co-auteurs.
        """
        self.co_auteurs = co_auteurs

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant le document Arxiv.

        Returns:
            str: La représentation du document Arxiv.
        """
        listeco = "\n"
        for co in self.co_auteurs:
            listeco += co + ",\n"
        return super().__str__() + f"\tCo-auteurs : {listeco}"
