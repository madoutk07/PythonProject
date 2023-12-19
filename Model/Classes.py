# Correction de G. Poux-Médard, 2021-2022

# =============== 2.1 : La classe Document ===============


class Document:
    # Initialisation des variables de la classe
    def __init__(self, titre="", auteur="", date="", url="", texte="" ):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

# =============== 2.2 : REPRESENTATIONS ===============
    # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(classe)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\tType : {self.getType()}"

    # Fonction qui renvoie le texte à afficher lorsqu'on tape str(classe)
    def __str__(self):
        return f"{self.titre}, par {self.auteur}"

    def  getType(self):
        pass



# =============== 2.4 : La classe Author ===============
class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = []
# =============== 2.5 : ADD ===============
    def add(self, production):
        self.ndoc += 1
        self.production.append(production)
    def __str__(self):
        return f"Auteur : {self.name}\t# productions : {self.ndoc}"



# =============== TD5.1 : rEDDITdOCUMENT ===============
class  RedditDocument(Document):
    def __init__(self, titre="", auteur="", date="", url="", texte="", nbcommentaires=0):
        super().__init__(titre, auteur, date, url, texte)
        self.nbcommentaires = nbcommentaires

    def  getNbcommentaires(self):
        return self.nbcommentaires

    def setNbcommentaires(self, nbcommentaires):
        self.nbcommentaires = nbcommentaires

    def __str__(self):
        return super().__str__() + f"\tNombre de commentaires : {self.nbcommentaires}"

    # =============== 5.3 ajout de  getType   ===============
    def  getType(self):
        return "Reddit"



# =============== TD5. 2 : ArxivDocument ===============

class  ArxivDocument(Document):
    def __init__(self, titre="", auteur="", date="", url="", texte="", co_auteurs=[]):
        self.co_auteurs = co_auteurs
        super().__init__(titre, auteur, date, url, texte)

    # =============== 5.3 ajout de  getType   ===============
    def  getType(self):

        return "Arxiv"

    def getCo_auteurs(self):
        return self.co_auteurs

    def  setCo_auteurs(self, co_auteurs):
        self.co_auteurs = co_auteurs

    def __str__(self):
        listeco = "\n"
        for co in self.co_auteurs:
            listeco += co + ",\n"
        return  super().__str__() + f"\tCo-auteurs : {listeco}"
