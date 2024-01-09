import unittest
# from Model.Classes import ArxivDocument, RedditDocument, DocumentGenerator
from Model.Corpus import Document, Author, RedditDocument, ArxivDocument
from Model.patterns import DocumentGenerator

class TestDocumentGenerator(unittest.TestCase):

    def test_factory_with_reddit_document(self):
        titre = "Titre"
        auteur = "Auteur"
        date = "2022-01-01"
        url = "https://example.com"
        texte = "Contenu du document"
        nbcommentaires = 10

        document = DocumentGenerator.factory(titre, auteur, date, url, texte, nbcommentaires)

        self.assertIsInstance(document, RedditDocument)
        self.assertEqual(document.titre, titre)
        self.assertEqual(document.auteur, auteur)
        self.assertEqual(document.date, date)
        self.assertEqual(document.url, url)
        self.assertEqual(document.texte, texte)
        self.assertEqual(document.nbcommentaires, nbcommentaires)

    def test_factory_with_arxiv_document(self):
        titre = "Titre"
        auteur = "Auteur"
        date = "2022-01-01"
        url = "https://example.com"
        texte = "Contenu du document"
        co_auteurs = ["Co-Auteur 1", "Co-Auteur 2"]

        document = DocumentGenerator.factory(titre, auteur, date, url, texte, co_auteurs=co_auteurs)

        self.assertIsInstance(document, ArxivDocument)
        self.assertEqual(document.titre, titre)
        self.assertEqual(document.auteur, auteur)
        self.assertEqual(document.date, date)
        self.assertEqual(document.url, url)
        self.assertEqual(document.texte, texte)
        self.assertEqual(document.co_auteurs, co_auteurs)

    def test_factory_with_no_optional_parameters(self):
        titre = "Titre"
        auteur = "Auteur"
        date = "2022-01-01"
        url = "https://example.com"
        texte = "Contenu du document"

        with self.assertRaises(AssertionError):
            DocumentGenerator.factory(titre, auteur, date, url, texte)

if __name__ == '__main__':
    unittest.main()
