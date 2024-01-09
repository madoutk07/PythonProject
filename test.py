from Model.Corpus import Corpus
from acquisition import scrapper


a = Corpus.load("Data/corpus.pkl")
voc = a.construire_vocabulaire()
a.calculer_occurences()
# # print(type(a))
# print(a.concorde("Iphone", 15))
print(a.freq)
# print(a.id2doc[0].texte)
# texte = "Bonjour, je m'appellé Jean2."
# print(texte)
# texte =Corpus.nettoyer_texte(texte)
# print(texte)
