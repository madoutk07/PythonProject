import praw
import urllib, urllib.request
import xmltodict

from Model.Corpus import Corpus
import datetime
from Model.Author import Author
from Model.patterns import DocumentGenerator



def  scrapper(query_terms,limit):

    docs_bruts = []
    afficher_cles = False

    for subreddit_name in query_terms:
        print(subreddit_name)
        tempLimit = limit
        j= 0
        while tempLimit > 0:
            try:
                reddit = praw.Reddit(client_id='lmT3q2vI0dfLlYW2M-5-sQ', client_secret='9c-0mjK4btAqm2mRIxcPCCCmTbucnQ', user_agent='projet_lyon')
                subreddit = reddit.subreddit(subreddit_name)
                hot_posts = subreddit.hot(limit=tempLimit)
                for post in hot_posts:
                    print(subreddit_name)
                    if afficher_cles:
                        for k, v in post.__dict__.items():
                            pass
                            print(k, ":", v)

                    temp = post.selftext.replace("\n", " ")
                    if(len(temp)<20):
                        continue
                    j += 1
                    tempLimit -= 1
                    print("Reddit:", j, "/", limit)
                    docs_bruts.append(("Reddit", post))
            except:
                print(subreddit_name)
                break

    for elemnt in query_terms:
        tempLimit = limit
        while tempLimit > 0:
            try:
                url = f'http://export.arxiv.org/api/query?search_query=all:{"+".join(elemnt)}&start=0&max_results={tempLimit}'
                data = urllib.request.urlopen(url)
                data = xmltodict.parse(data.read().decode('utf-8'))
                j= 0
                for i, entry in enumerate(data["feed"]["entry"]):
                    temp = entry["summary"].replace("\n", " ")
                    if(len(temp)<20):
                        continue
                    j += 1
                    print("ArXiv:", j, "/", limit)
                    docs_bruts.append(("ArXiv", entry))
                    tempLimit -= 1
            except:
                break


    collection = []
    for nature, doc in docs_bruts:
        if nature == "ArXiv":
            titre = doc["title"].replace('\n', '')
            try:
                temp = ",".join([a["name"] for a in doc["author"]])
                authors = temp.split(",")
                auteur = authors[0]
                authors = authors[1:]
                print("auteur",auteur)
                print("coauteur",authors)
            except:
                authors = doc["author"]["name"]
                auteur = authors
                authors= []

            summary = doc["summary"].replace("\n", "")
            date = datetime.datetime.strptime(doc["published"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")
            doc_classe= DocumentGenerator.factory(titre, auteur, date, doc["id"], summary, co_auteurs=authors)
            collection.append(doc_classe)

        elif nature == "Reddit":
            titre = doc.title.replace("\n", '')
            auteur = str(doc.author)
            date = datetime.datetime.fromtimestamp(doc.created).strftime("%Y/%m/%d")
            url = "https://www.reddit.com/"+doc.permalink
            texte = doc.selftext.replace("\n", "")
            nbcommentaire = int(doc.num_comments)
            doc_classe= DocumentGenerator.factory(titre, auteur, date, url, texte, nbcommentaires=nbcommentaire)
            collection.append(doc_classe)


    # Création de l'index de documents
    id2doc = {}
    ndoc = 0
    for i, doc in enumerate(collection):
        ndoc += 1
        id2doc[doc.titre] = doc

    # Création de la liste+index des Auteurs
    authors = {}
    naut = 0
    for i, doc in enumerate(collection):
        if doc.auteur not in authors.keys():
            naut += 1
            temp = Author(doc.auteur)
            authors[doc.auteur] = temp
            authors[doc.auteur].add(doc.titre)
        else:
            authors[doc.auteur].add(doc.titre)

        try:

            for co_auteur in doc.getCo_auteurs():

                if co_auteur not in authors.keys():
                    # print("co",co_auteur)
                    naut += 1
                    temp = Author(co_auteur)
                    authors[co_auteur] = temp
                    authors[co_auteur].add(doc.titre)
                else:
                    authors[co_auteur].add(doc.titre)
        except :
            # print('bug')
            pass
    # Construction du corpus à partir des documents et des auteurs
    corpus = Corpus("Mon corpus")
    for doc in authors.values():
        corpus.add_Author(doc)

    for doc in id2doc.values():
        corpus.add_Document(doc)
    return  corpus



