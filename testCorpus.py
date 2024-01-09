# Correction de G. Poux-Médard, 2021-2022

import pickle
import pandas as pd
import re

from Model.Classes import Author
from Model.patterns import singleton
from Model.patterns import DocumentGenerator


class Corpus:
    """
    Classe représentant un corpus de documents.

    Attributes:
        passages : Chaîne de caractères contenant tous les passages des documents du corpus.
        nom : Nom du corpus.
        authors : Dictionnaire des auteurs du corpus.
        aut2id : Dictionnaire faisant correspondre chaque auteur à un identifiant unique.
        id2doc : Dictionnaire faisant correspondre chaque identifiant de document à un objet de document.
        ndoc : Nombre total de documents dans le corpus.
        naut : Nombre total d'auteurs dans le corpus.
    """

    passages = ""

    def __init__(self, nom):
        """
        Initialise une instance de la classe Corpus.

        Args:
            nom : Nom du corpus.
        """
        self.nom = nom
        self.authors = {}
        self.aut2id = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0

    def add(self, doc):
        """
        Ajoute un document au corpus.

        Args:
            doc (ArxivDocument or RedditDocument): Objet de document à ajouter.
        """
        if doc.auteur not in self.aut2id:
            self.naut += 1
            self.authors[self.naut] = Author(doc.auteur)
            self.aut2id[doc.auteur] = self.naut
        self.authors[self.aut2id[doc.auteur]].add(doc.texte)
        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

    def show(self, n_docs=-1, tri="abc"):
        """
        Affiche les documents du corpus.

        Args:
            n_docs (int, optional): Nombre de documents à afficher. -1 pour afficher tous les documents. Par défaut -1.
            tri (str, optional): Méthode de tri des documents. "abc" pour un tri alphabétique, "123" pour un tri temporel. Par défaut "abc".
        """
        docs = list(self.id2doc.values())
        if tri == "abc":
            docs = list(sorted(docs, key=lambda x: x.titre.lower()))[:n_docs]
        elif tri == "123":
            docs = list(sorted(docs, key=lambda x: x.date))[:n_docs]

        print("\n".join(list(map(repr, docs))))

    def __repr__(self):
        """
        Renvoie une représentation en chaîne de caractères du corpus.

        Returns:
            str: Représentation en chaîne de caractères du corpus.
        """
        docs = list(self.id2doc.values())
        docs = list(sorted(docs, key=lambda x: x.titre.lower()))

        return "\n".join(list(map(str, docs)))

    def save(self, filename):
        """
        Sauvegarde le corpus dans un fichier binaire.

        Args:
            filename (str): Nom du fichier de sauvegarde.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        """
        Charge un corpus à partir d'un fichier binaire.

        Args:
            filename (str): Nom du fichier à charger.

        Returns:
            Corpus: Objet de corpus chargé à partir du fichier.
        """
        with open(filename, 'rb') as f:
            corpusLoad = pickle.load(f)
        return corpusLoad

    def construireChaine(self):
        """
        Construit une chaîne de caractères contenant tous les passages des documents du corpus.

        Returns:
            str: Chaîne de caractères contenant tous les passages des documents du corpus.
        """
        if self.passages == "":
            for doc in self.id2doc.values():
                self.passages = self.passages + doc.texte
        return self.passages

    def search(self, aTrouver):
        """
        Recherche un motif dans la chaîne de caractères du corpus.

        Args:
            aTrouver (str): Motif à rechercher.

        Returns:
            re.MatchIterator: Itérateur contenant les correspondances trouvées.
        """
        s = re.finditer(aTrouver, self.construireChaine())
        return s

    def concorde(self, aTrouver, nb):
        """
        Renvoie un DataFrame contenant les contextes gauche, le motif trouvé et les contextes droits pour un motif donné.

        Args:
            aTrouver (str): Motif à rechercher.
            nb (int): Nombre de caractères à inclure dans les contextes gauche et droit.

        Returns:
            pd.DataFrame: DataFrame contenant les contextes gauche, le motif trouvé et les contextes droits.
        """
        s = self.search(aTrouver)
        contexteG = []
        contexteC = []
        contexteD = []
        for a in s:
            spn = a.span()
            contexteG.append(self.passages[spn[0] - nb:spn[0]])
            contexteC.append(aTrouver)
            contexteD.append(self.passages[spn[1]:spn[1] + nb])
        df = pd.DataFrame({'contexte gauche': contexteG, 'motif trouve': contexteC, 'contexte droit': contexteD})

        return df

    def nettoyer_texte(self, chaine):
        """
        Nettoie une chaîne de caractères en la mettant en minuscules, en supprimant les caractères spéciaux, les chiffres, les tabulations et les retours à la ligne.

        Args:
            chaine (str): Chaîne de caractères à nettoyer.

        Returns:
            str: Chaîne de caractères nettoyée.
        """
        chaine = chaine.lower()
        chaine = re.sub(r'\n', "", chaine)
        chaine = re.sub(r'\t', "", chaine)
        chaine = re.sub(r'[^\w\s]', "", chaine)
        chaine = re.sub(r'\d', "", chaine)

        return chaine

    def count_word_occurrences(self):
        """
        Compte le nombre d'occurrences de chaque mot dans le corpus.

        Returns:
            pd.DataFrame: Tableau de fréquence contenant les mots et leur compte.
        """
        vocabulary = self.construire_dictionnaire()
        word_counts = {}

        for doc in self.id2doc.values():
            words = self.nettoyer_texte(doc.texte)
            words = re.split(' ', words)
            for word in words:
                if word in vocabulary:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

        freq_table = pd.DataFrame({'Word': list(word_counts.keys()), 'Count': list(word_counts.values())})
        return freq_table

    def construire_dictionnaire(self):
        """
        Construit un dictionnaire de mots à partir des documents du corpus.

        Returns:
            set: Dictionnaire de mots.
        """
        vocabulary = set()
        compteur = 0
        for doc in self.id2doc.values():
            words = self.nettoyer_texte(doc.texte)
            words = re.split(' ', words)
            vocabulary.update(words)
        return vocabulary
