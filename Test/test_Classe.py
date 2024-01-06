import unittest
from model.corpus import Document, Author, RedditDocument, ArxivDocument
class TestCorpus(unittest.TestCase):

    def test_document(self):
        doc = Document("Title", "Author", "2022-01-01", "www.example.com", "This is the text")
        self.assertEqual(doc.titre, "Title")
        self.assertEqual(doc.auteur, "Author")
        self.assertEqual(doc.date, "2022-01-01")
        self.assertEqual(doc.url, "www.example.com")
        self.assertEqual(doc.texte, "This is the text")

    def test_author(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertEqual(author.ndoc, 0)
        self.assertEqual(author.production, [])

        author.add("Production 1")
        self.assertEqual(author.ndoc, 1)
        self.assertEqual(author.production, ["Production 1"])

    def test_reddit_document(self):
        reddit_doc = RedditDocument("Title", "Author", "2022-01-01", "www.example.com", "This is the text", 10)
        self.assertEqual(reddit_doc.titre, "Title")
        self.assertEqual(reddit_doc.auteur, "Author")
        self.assertEqual(reddit_doc.date, "2022-01-01")
        self.assertEqual(reddit_doc.url, "www.example.com")
        self.assertEqual(reddit_doc.texte, "This is the text")
        self.assertEqual(reddit_doc.nbcommentaires, 10)

    def test_arxiv_document(self):
        arxiv_doc = ArxivDocument("Title", "Author", "2022-01-01", "www.example.com", "This is the text", ["Co-author 1", "Co-author 2"])
        self.assertEqual(arxiv_doc.titre, "Title")
        self.assertEqual(arxiv_doc.auteur, "Author")
        self.assertEqual(arxiv_doc.date, "2022-01-01")
        self.assertEqual(arxiv_doc.url, "www.example.com")
        self.assertEqual(arxiv_doc.texte, "This is the text")
        self.assertEqual(arxiv_doc.co_auteurs, ["Co-author 1", "Co-author 2"])

if __name__ == '__main__':
    unittest.main()
