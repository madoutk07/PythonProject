
class Author:
    """
    Classe représentant un auteur.

    Attributes:
        name (str): Le nom de l'auteur.
        ndoc (int): Le nombre de documents produits par l'auteur.
        production (list): La liste des productions de l'auteur.
    """
    def __init__(self, name):
        """
        Initialise une instance de la classe Author.

        Args:
            name (str): Le nom de l'auteur.
        """
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
        return f"Auteur : {self.name}\t# nombreproductions : {self.ndoc}"
