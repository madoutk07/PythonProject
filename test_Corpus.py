import pytest
from Model import Corpus
from Model import Author
import pytest
from Model import ArxivDocument

def test_corpus_add_author():
    corpus = Corpus("Test")
    author = Author("testauthor")
    corpus.add_Author(author)

    assert len(corpus.authors) == 1
    assert corpus.authors["testauthor"] == author
    assert corpus.naut == 1

def test_corpus_add_document():
    corpus = Corpus("Test")
    document = ArxivDocument(titre="titre", auteur="auteur", date="10/10/2010", url="https://example.com", texte="textetexte", co_auteurs=["me","you"])
    corpus.add_Document(document)

    assert len(corpus.id2doc) == 1
    assert corpus.id2doc[0] == document
    assert corpus.ndoc == 1

def test_corpus_save_load(tmp_path):
    corpus = Corpus("Test")
    document = ArxivDocument(titre="titre", auteur="auteur", date="10/10/2010", url="https://example.com", texte="textetexte", co_auteurs=["me","you"])
    corpus.add_Document(document)

    filename = tmp_path / "corpus.pkl"
    corpus.save(filename)

    loaded_corpus = Corpus.load(filename)

    assert loaded_corpus.nom == "Test"
    assert len(loaded_corpus.id2doc) == 1
    assert loaded_corpus.id2doc[0].texte == "textetexte"



