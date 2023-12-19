# Correction de G. Poux-Médard, 2021-2022

# from Classes import Author

# from Model.Classes import ArxivDocument, RedditDocument
import pickle
from Model.Classes import Author
from Model.patterns import singleton
import  pandas  as  pd
import  re
import re
import pandas as pd
# =============== 2.7 : CLASSE CORPUS ===============
# @singleton
class Corpus:
    passages = ""
    def __init__(self, nom):
        self.nom = nom
        self.authors = {}
        self.aut2id = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0

    def add(self, doc):
        if doc.auteur not in self.aut2id:
            self.naut += 1
            self.authors[self.naut] = Author(doc.auteur)
            self.aut2id[doc.auteur] = self.naut
        self.authors[self.aut2id[doc.auteur]].add(doc.texte)
        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

# =============== 2.8 : REPRESENTATION ===============
    def show(self, n_docs=-1, tri="abc"):
        docs = list(self.id2doc.values())
        if tri == "abc":  # Tri alphabétique
            docs = list(sorted(docs, key=lambda x: x.titre.lower()))[:n_docs]
        elif tri == "123":  # Tri temporel
            docs = list(sorted(docs, key=lambda x: x.date))[:n_docs]

        print("\n".join(list(map(repr, docs))))


    def __repr__(self):
        docs = list(self.id2doc.values())
        docs = list(sorted(docs, key=lambda x: x.titre.lower()))

        return "\n".join(list(map(str, docs)))


    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    def load(filename):
                with open(filename, 'rb') as f:
                    corpusLoad = pickle.load(f)
                return corpusLoad
    # @singleton
    def  construireChaine(self):
        if  self.passages == "":
            for doc in self.id2doc.values():
                    # self.passages.append(doc.texte)
                    # print(doc.texte)
                    self.passages = self.passages + doc.texte
        return self.passages


    def search(self, aTrouver):
        s = re.finditer(aTrouver, self.construireChaine())
        return s

    def  concorde(self,aTrouver ,nb):
        s = self.search(aTrouver)
        contexteG = []
        contexteC = []
        contexteD = []
        for a in  s:
              spn = a.span()
              contexteG.append(self.passages[spn[0]-nb:spn[0]])
              contexteC.append(aTrouver)
              contexteD.append(self.passages[spn[1]:spn[1]+nb])
        df = pd.DataFrame({'contexte gauche':contexteG , 'motif trouve':contexteC ,  'contexte  droit':contexteD })

        return  df

    def nettoyer_texte(self,chaine):
        chaine = chaine.lower()
        chaine = re.sub(r'\n', "", chaine)
        chaine = re.sub(r'\t', "", chaine)
        chaine = re.sub(r'[^\w\s]', "", chaine)
        chaine = re.sub(r'\d', "", chaine)

        return chaine


    def count_word_occurrences(self):
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
        vocabulary = set()
        compteur = 0
        for doc in self.id2doc.values():
            words = self.nettoyer_texte(doc.texte)    # Fix: Call nettoyer_texte using self
            words = re.split(' ', words)
            vocabulary.update(words)
        return vocabulary


