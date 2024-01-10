import  Model.Corpus as Corpus
from difflib import SequenceMatcher

def comparerAuteur(a, b):
    return SequenceMatcher(None, a, b).ratio()



def FaireVocabulaire(phrase):
    vocab =  set()
    phrase= Corpus.nettoyer_texte(phrase)
    phrase  = phrase.split(' ')
    phrase = [mot for mot in phrase if mot != '']
    vocab.update(phrase)
    return  vocab

def RechercherTfIdf(phrase, corpus):
    vocab = FaireVocabulaire(phrase)
    similarite = corpus.calculer_similarite_TFxIDF(vocab)
    ListeDoc = []
    for  id, score in similarite:

        dic={
            "titre": corpus.id2doc[id].titre,
            "auteur": corpus.id2doc[id].auteur,
            "date": corpus.id2doc[id].date,
            "url": corpus.id2doc[id].url,
            "texte": corpus.id2doc[id].texte[:100],
            "source": corpus.id2doc[id].getType(),
            "score": score
        }
        # print(dic)
        ListeDoc.append(dic)

    return ListeDoc
    # print(ListeDoc[:3])
def RechercherTf(phrase, corpus):
    vocab = FaireVocabulaire(phrase)
    similarite = corpus.calculer_similarite_TF(vocab)
    ListeDoc = []
    for  id, score in similarite:

        dic={
            "titre": corpus.id2doc[id].titre,
            "auteur": corpus.id2doc[id].auteur,
            "date": corpus.id2doc[id].date,
            "url": corpus.id2doc[id].url,
            "texte": corpus.id2doc[id].texte[:100],
            "source": corpus.id2doc[id].getType(),
            "score": score
        }
        # print(dic)
        ListeDoc.append(dic)

    return ListeDoc
    # print(ListeDoc[:3])



def RechercherAuteur(NomAuteur, corpus):
    ListeDoc = []
    for auteur  in corpus.authors.values():
        temp = comparerAuteur(auteur.name, NomAuteur)
        if temp > 0.5:
            for  titre  in  auteur.production:
                for  elemnt  in    corpus.id2doc.values():
                    if  elemnt.titre == titre:
                        dic={
                                    "titre": elemnt.titre,
                                    "auteur": elemnt.auteur,
                                    "date": elemnt.date,
                                    "url": elemnt.url,
                                    "texte": elemnt.texte[:100],
                                    "source": elemnt.getType(),
                                    "score": temp
                                }
                        ListeDoc.append(dic)
                        break
    return ListeDoc





#     # vocab = FaireVocabulaire(phrase)
#     # similarite = corpus.calculer_similarite_TF(vocab)
#     # ListeDoc = []
#     # for  id, score in similarite:

#     #     dic={
#     #         "titre": corpus.id2doc[id].titre,
#     #         "auteur": corpus.id2doc[id].auteur,
#     #         "date": corpus.id2doc[id].date,
#     #         "url": corpus.id2doc[id].url,
#     #         "texte": corpus.id2doc[id].texte[:100],
#     #         "source": corpus.id2doc[id].getType(),
#     #         "score": score
#     #     }
#     #     # print(dic)
#     #     ListeDoc.append(dic)

#     # return ListeDoc
#     # # print(ListeDoc[:3])


# a = Corpus.load("Data/corpus.pkl")
# # a.construire_mat_TFxIDF()
# # print(a.mat_TFxIDF)

# # b = FaireVocabulaire("Bonjour, je m'appelle Jean2. je  veux un  iphone")
# # a.calculer_similarite_TF(b)
# # a.calculer_similarite_TFxIDF(b)
# # RechercherTfIdf("Bonjour, je m'appelle Jean2. je  veux un  iphone", a)
# # print()
# d  = RechercherAuteur("Dense_Masterpiece_42", a)
# print(d[0])
# # print(a.id2doc[ 1])