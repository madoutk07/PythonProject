from Model.Corpus import Corpus
from acquisition import scrapper


a = Corpus.load("Data/corpus.pkl")
print(len(a.id2doc))
# voc = a.construire_vocabulaire()
# # a.calculer_occurences()
# a.construire_mat_TF()
# # print(type(a))
# print(a.concorde("Iphone", 15))
# print(a.mat_TF)
# a.construire_vocab()
# print(a.vocab)
# a.construire_mat_TFxIDF()
# print(a.mat_TFxIDF)
# print(a.mat_TF[1,1])
# print(a.id2doc[0].texte)
# texte = "Bonjour, je m'appellé Jean2."
# print(texte)
# texte =Corpus.nettoyer_texte(texte)
# print(texte)
