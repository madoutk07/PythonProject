# Correction de G. Poux-Médard, 2021-2022

import pickle
import pandas as pd
import re
from Model.patterns import singleton
import pandas as pd
from unidecode import unidecode

# @singleton
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



    def __init__(self, nom):
        """
        Initialise une instance de la classe Corpus.

        Args:
            nom : Nom du corpus.
        """
        self.nom = nom
        self.authors = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0
        self.passages = ""
        self.freq = None

    def add_Author(self, auteur):
        nom =auteur.name
        if nom not in self.authors.keys():
            self.authors[nom]=auteur
            self.naut+=1

    def add_Document(self, doc):
        if doc not in self.id2doc.values():
            self.id2doc[self.ndoc]= doc
            self.ndoc+=1

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

        docs =[f"{key} {value}" for key , value in self.id2doc.items()]
        aut = [f"{key} {value}" for key , value in self.authors.items()]

        temp = "\n".join(list(map(str, docs)))
        temp += "\n".join(list(map(str, aut)))
        return temp

    def save(self, filename):
        """
        Sauvegarde le corpus dans un fichier binaire et un fichier JSON.

        Args:
            filename (str): Nom du fichier de sauvegarde.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

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
            self.passages = " ".join([docu.texte for docu in self.id2doc.values()])
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

    def nettoyer_texte(chaine):
        """
        Nettoie une chaîne de caractères en la mettant en minuscules, en supprimant les caractères spéciaux, les chiffres, les tabulations et les retours à la ligne.

        Args:
            chaine (str): Chaîne de caractères à nettoyer.

        Returns:
            str: Chaîne de caractères nettoyée.
        """

        # convertit tous les caractères de la chaîne  en minuscules
        chaine = chaine.lower()

        # substituer toutes les occurrences de caractères de saut de ligne (\n) et (\t) par ""
        chaine = re.sub(r'\n', " ", chaine)
        chaine = re.sub(r'\t', " ", chaine)

        # supprimer tous les caractères non alphanumériques
        chaine = re.sub(r'[^\w\s]', " ", chaine)
        # supprime tous les chiffres  de la chaîne
        chaine = re.sub(r'\d', " ", chaine)

        # caractères accentués en caractères non accentués
        chaine = unidecode(chaine)

        return chaine


    def construire_vocabulaire(self):
        """
        Construit un vocabulaire à partir du texte de chaque document.

        Returns:
            dict: Dictionnaire représentant le vocabulaire.
        """
        # Initialiser le vocabulaire
        voc = set()
        for cle, document in self.id2doc.items():
            # cle = document.titre
            mots = Corpus.nettoyer_texte(document.texte)
            mots  = mots.split(' ')
            mots = [mot for mot in mots if mot != '']
            voc.update(mots)
        return voc

    def stats(self):

        vocabulaire = self.construire_vocabulaire()
        frequences_mot = {mot: 0 for mot in vocabulaire}
        frequences_document = {mot: 0 for mot in vocabulaire}

        for cle, document in self.id2doc.items():
            tempdoc = [True for _ in vocabulaire]
            mots = Corpus.nettoyer_texte(document.texte)
            mots = mots.split(' ')
            for mot in mots:
                if mot in vocabulaire:

                    indexMot = list(vocabulaire).index(mot)

                    if tempdoc[indexMot]:
                        frequences_document[mot] += 1
                        tempdoc[indexMot] = False

                    if mot in frequences_mot:
                        frequences_mot[mot] += 1

        final = [{'Mot': mot, 'Frequence_mot': frequences_mot[mot], 'Frequence_document': frequences_document[mot]} for mot in vocabulaire]
        self.freq = pd.DataFrame(final)
