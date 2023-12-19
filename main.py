# Correction de G. Poux-Médard, 2021-2022

# =============== PARTIE 1 =============
# =============== 1.1 : REDDIT ===============
# Library
import praw
import pickle
import urllib, urllib.request
import xmltodict
from Model.Classes import Document
from Model.Corpus import Corpus
import datetime
from Model.Classes import Author
from Model.patterns import DocumentGenerator

# Fonction affichage hiérarchie dict
def showDictStruct(d):
    def recursivePrint(d, i):
        for k in d:
            if isinstance(d[k], dict):
                print("-"*i, k)
                recursivePrint(d[k], i+2)
            else:
                print("-"*i, k, ":", d[k])
    recursivePrint(d, 1)

# Identification
# reddit = praw.Reddit(client_id='XXXXXX', client_secret='YYYYY', user_agent='ZZZZZ')
def  scrapper(query_terms,limit):


    reddit = praw.Reddit(client_id='lmT3q2vI0dfLlYW2M-5-sQ', client_secret='9c-0mjK4btAqm2mRIxcPCCCmTbucnQ', user_agent='projet_lyon')
    # hot_posts = reddit.subreddit(query_terms).hot(limit=limit)#.top("all", limit=limit)#
    # /subr =  reddit.subreddit(redditSubject)
    docs = []
    docs_bruts = []
    afficher_cles = True
    for subreddit_name in query_terms:
        subreddit = reddit.subreddit(subreddit_name)
        hot_posts = subreddit.hot(limit=limit)

        # print(f"Hot posts in {subreddit_name}:")
        # for post in hot_posts:
        #     print(post.title)
        # print("\n")

        for i, post in enumerate(hot_posts):
            if i%10==0: print("Reddit:", i, "/", limit)
            if afficher_cles:  # Pour connaître les différentes variables et leur contenu
                for k, v in post.__dict__.items():
                    pass
                    print(k, ":", v)

            if post.selftext != "":  # Osef des posts sans texte
                pass
                #print(post.selftext)
            docs.append(post.selftext.replace("\n", " "))
            docs_bruts.append(("Reddit", post))


        # Requête
    url = f'http://export.arxiv.org/api/query?search_query=all:{"+".join(query_terms)}&start=0&max_results={limit}'
    data = urllib.request.urlopen(url)
    # Format dict (OrderedDict)
    data = xmltodict.parse(data.read().decode('utf-8'))
    for i, entry in enumerate(data["feed"]["entry"]):
            if i%10==0: print("ArXiv:", i, "/", limit)
            docs.append(entry["summary"].replace("\n", ""))
            docs_bruts.append(("ArXiv", entry))
            #showDictStruct(entry)

    print(f"# docs avec doublons : {len(docs)}")
    docs = list(set(docs))
    print(f"# docs sans doublons : {len(docs)}")

    for i, doc in enumerate(docs):
        print(f"Document {i}\t# caractères : {len(doc)}\t# mots : {len(doc.split(' '))}\t# phrases : {len(doc.split('.'))}")
        if len(doc)<100:
            docs.remove(doc)
    longueChaineDeCaracteres = " ".join(docs)


    collection = []
    for nature, doc in docs_bruts:
        if nature == "ArXiv":  # Les fichiers de ArXiv ou de Reddit sont pas formatés de la même manière à ce stade.
            #showDictStruct(doc)

            titre = doc["title"].replace('\n', '')  # On enlève les retours à la ligne
            try:
                authors = ", ".join([a["name"] for a in doc["author"]])  # On fait une liste d'auteurs, séparés par une virgule
                auteur = authors[0]
                authors = authors[1:]
            except:
                authors = doc["author"]["name"]  # Si l'auteur est seul, pas besoin de liste
                auteur = authors
                authors= []

            summary = doc["summary"].replace("\n", "")  # On enlève les retours à la ligne
            date = datetime.datetime.strptime(doc["published"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")  # Formatage de la date en année/mois/jour avec librairie datetime

            doc_classe= DocumentGenerator.factory(titre, auteur, date, doc["id"], summary, co_auteurs=authors)
            # doc_classe = Document(titre, authors, date, doc["id"], summary)  # Création du Document
            collection.append(doc_classe)  # Ajout du Document à la liste.

        elif nature == "Reddit":
            #print("".join([f"{k}: {v}\n" for k, v in doc.__dict__.items()]))
            titre = doc.title.replace("\n", '')
            auteur = str(doc.author)
            date = datetime.datetime.fromtimestamp(doc.created).strftime("%Y/%m/%d")
            url = "https://www.reddit.com/"+doc.permalink
            texte = doc.selftext.replace("\n", "")
            nbcommentaire = int(doc.num_comments)
            print(nbcommentaire)
            doc_classe= DocumentGenerator.factory(titre, auteur, date, url, texte, nbcommentaires=nbcommentaire)
            # doc_classe = Document(titre, auteur, date, url, texte)
            collection.append(doc_classe)

    # Création de l'index de documents
    id2doc = {}
    for i, doc in enumerate(collection):
        id2doc[i] = doc.titre

# =============== 2.4, 2.5 : CLASSE AUTEURS ===============


# =============== 2.6 : DICT AUTEURS ===============
    authors = {}
    aut2id = {}
    num_auteurs_vus = 0

# Création de la liste+index des Auteurs
    for doc in collection:
        if doc.auteur not in aut2id:
            num_auteurs_vus += 1
            authors[num_auteurs_vus] = Author(doc.auteur)
            aut2id[doc.auteur] = num_auteurs_vus
        authors[aut2id[doc.auteur]].add(doc.texte)


    # =============== 2.7, 2.8 : CORPUS ===============
    corpus = Corpus("Mon corpus")
    # Construction du corpus à partir des documents
    for doc in collection:
        corpus.add(doc)
    return  corpus


# corpus = Corpus("Mon corpus")
corpusi = scrapper(["Iphone"],13)
corpusi.save("Data/corpusi.pkl")
print(type(corpusi))
# corpusi.show(tri="abc")
# print(repr(corpusi))

a= corpusi.construire_vocabulaire()
print(a)

# a = corpusi.concorde("iphone",100)

# print(a.head())

# a = corpusi.search("iphone")


# for match in a:
#     print(match.span())

# print(corpusi.construireChaine())


# =============== 2.9 : SAUVEGARDE ===============


# corpusa = Corpus("Monwq corpus")
# corpusa.show(tri="abc")

# corpus.save("Data/corpusi.pkl")
# del(corpus)
# # print(corpus)

# corpusa = Corpus("Mon corpus")
# corpusa =  Corpus.load("Data/corpusi.pkl")
# print(corpusa)










