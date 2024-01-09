from Model.Corpus import Corpus
from acquisition import scrapper

def main():
    """
    Fonction principale du programme.
    Effectue le scrapping d'un corpus de données en utilisant les mots-clés spécifiés.
    Sauvegarde le corpus dans un fichier pickle.
    Charge le corpus à partir du fichier pickle et l'affiche.
    """
    corpusi = scrapper(["Iphone"], 100)
    corpusi.save("Data/corpus.pkl")

    del corpusi

    a = Corpus.load("Data/corpus.pkl")
    print(type(a))
    print(a)

main()
