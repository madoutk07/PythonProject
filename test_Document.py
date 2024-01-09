import pytest
from Model import Document
import pytest
from Model import RedditDocument, ArxivDocument




def test_reddit_document_init():
    reddit_doc = RedditDocument("Title", "Author", "2022-01-01", "https://example.com", "textetexte", 10)
    assert reddit_doc.titre == "Title"
    assert reddit_doc.auteur == "Author"
    assert reddit_doc.date == "2022-01-01"
    assert reddit_doc.url == "https://example.com"
    assert reddit_doc.texte == "textetexte"
    assert reddit_doc.getNbcommentaires() == 10

def test_reddit_document_str():
    reddit_doc = RedditDocument("Title", "Author", "2022-01-01", "https://example.com", "textetexte", 10)
    assert str(reddit_doc) == "Title, par Author\tNombre de commentaires : 10"

def test_reddit_document_get_type():
    reddit_doc = RedditDocument("Title", "Author", "2022-01-01", "https://example.com", "textetexte", 10)
    assert reddit_doc.getType() == "Reddit"

def test_arxiv_document_init():
    arxiv_doc = ArxivDocument("Title", "Author", "2022-01-01", "https://example.com", "Sample text", ["me","you"])
    assert arxiv_doc.titre == "Title"
    assert arxiv_doc.auteur == "Author"
    assert arxiv_doc.date == "2022-01-01"
    assert arxiv_doc.url == "https://example.com"
    assert arxiv_doc.texte == "Sample text"
    assert arxiv_doc.getCo_auteurs() == ["me","you"]

def test_arxiv_document_get_type():
    arxiv_doc = ArxivDocument("Title", "Author", "2022-01-01", "https://example.com", "Sample text", ["me","you"])
    assert arxiv_doc.getType() == "Arxiv"

