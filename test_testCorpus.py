import pytest
from Model.Classes import Document, Author, RedditDocument, ArxivDocument

def test_document():
    doc = Document("Title", "Author", "2022-01-01", "www.example.com", "This is the text")
    assert doc.titre == "Title"
    assert doc.auteur == "Author"
    assert doc.date == "2022-01-01"
    assert doc.url == "www.example.com"
    assert doc.texte == "This is the text"

def test_author():
    author = Author("John Doe")
    assert author.name == "John Doe"
    assert author.ndoc == 0
    assert author.production == []

    author.add("Production 1")
    assert author.ndoc == 1
    assert author.production == ["Production 1"]

def test_reddit_document():
    reddit_doc = RedditDocument("Title", "Author", "2022-01-01", "www.example.com", "This is the text", 10)
    assert reddit_doc.titre == "Title"
    assert reddit_doc.auteur == "Author"
    assert reddit_doc.date == "2022-01-01"
    assert reddit_doc.url == "www.example.com"
    assert reddit_doc.texte == "This is the text"
    assert reddit_doc.nbcommentaires == 10

def test_arxiv_document():
    arxiv_doc = ArxivDocument("Title", "Author", "2022-01-01", "www.example.com", "This is the text", ["Co-author 1", "Co-author 2"])
    assert arxiv_doc.titre == "Title"
    assert arxiv_doc.auteur == "Author"
    assert arxiv_doc.date == "2022-01-01"
    assert arxiv_doc.url == "www.example.com"
    assert arxiv_doc.texte == "This is the text"
    assert arxiv_doc.co_auteurs == ["Co-author 1", "Co-author 2"]