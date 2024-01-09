import unittest
from Model.Corpus import Corpus
from Model.Classes import ArxivDocument, RedditDocument
import pandas as pd

class CorpusTest(unittest.TestCase):
    def setUp(self):
        self.corpus = Corpus("Test Corpus")
        self.doc1 = ArxivDocument("Author 1", "Document 1")
        self.doc2 = ArxivDocument("Author 2", "Document 2")
        self.doc3 = RedditDocument("Author 3", "Document 3")
        self.corpus.add(self.doc1)
        self.corpus.add(self.doc2)
        self.corpus.add(self.doc3)

    def test_add(self):
        self.assertEqual(len(self.corpus.authors), 3)
        self.assertEqual(len(self.corpus.id2doc), 3)
        self.assertEqual(self.corpus.ndoc, 3)
        self.assertEqual(self.corpus.naut, 3)

    def test_show(self):
        # Test sorting by title
        expected_output = "Document 1\nDocument 2\nDocument 3"
        self.assertEqual(self.corpus.show(n_docs=3, tri="abc"), expected_output)

        # Test sorting by date
        expected_output = "Document 1\nDocument 3\nDocument 2"
        self.assertEqual(self.corpus.show(n_docs=3, tri="123"), expected_output)

    def test_save_load(self):
        filename = "test_corpus.pkl"
        self.corpus.save(filename)
        loaded_corpus = Corpus.load(filename)
        self.assertEqual(self.corpus.nom, loaded_corpus.nom)
        self.assertEqual(len(self.corpus.authors), len(loaded_corpus.authors))
        self.assertEqual(len(self.corpus.id2doc), len(loaded_corpus.id2doc))
        self.assertEqual(self.corpus.ndoc, loaded_corpus.ndoc)
        self.assertEqual(self.corpus.naut, loaded_corpus.naut)

    def test_construireChaine(self):
        expected_output = "Document 1Document 2Document 3"
        self.assertEqual(self.corpus.construireChaine(), expected_output)

    def test_search(self):
        expected_output = ["Document 1", "Document 2", "Document 3"]
        self.assertEqual(list(self.corpus.search("Document")), expected_output)

    def test_concorde(self):
        expected_output = pd.DataFrame({
            'contexte gauche': ["nt 1", "nt 2", "nt 3"],
            'motif trouve': ["Document", "Document", "Document"],
            'contexte droit': ["ocume", "ocume", "ocume"]
        })
        self.assertEqual(self.corpus.concorde("Document", nb=3), expected_output)

    def test_nettoyer_texte(self):
        input_text = "This is a test text with special characters: !@#$%^&*()_+123"
        expected_output = "this is a test text with special characters "
        self.assertEqual(self.corpus.nettoyer_texte(input_text), expected_output)

    def test_count_word_occurrences(self):
        expected_output = pd.DataFrame({
            'Word': ["this", "is", "a", "test", "text", "with", "special", "characters"],
            'Count': [1, 1, 1, 1, 1, 1, 1, 1]
        })
        self.assertEqual(self.corpus.count_word_occurrences(), expected_output)

    def test_construire_dictionnaire(self):
        expected_output = {"this", "is", "a", "test", "text", "with", "special", "characters"}
        self.assertEqual(self.corpus.construire_dictionnaire(), expected_output)

if __name__ == '__main__':
    unittest.main()
