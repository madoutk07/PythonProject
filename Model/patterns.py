from Model.Classes import ArxivDocument, RedditDocument

# def singleton(cls):

#     instances = [None]
#     def wrapper(*args, **kwargs):
#         if instances[0]  is None:
#             instances[0] = cls(*args, **kwargs)
#         return instances[0]
#     return wrapper

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            try:
                instances[cls] = cls(*args, **kwargs)
                return instances[cls]
            except Exception:
                raise("bug")
        else:
              raise Exception("Instance already exists")
    return wrapper


class DocumentGenerator:
        @staticmethod
        def factory(titre, auteur, date, url, texte ,nbcommentaires = None, co_auteurs = None):
            if nbcommentaires is not None : return RedditDocument(titre, auteur, date, url, texte,nbcommentaires)
            if co_auteurs is not None          : return ArxivDocument(titre, auteur, date, url, texte, co_auteurs)
            assert 0, "erreur "+type


