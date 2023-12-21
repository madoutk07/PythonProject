import pytest

from Model import Corpus


def test_corpus_add():
    corpus = Corpus("Test Corpus")
    doc1 = "This is document 1"
    doc2 = "This is document 2"

    corpus.add(doc1)
    corpus.add(doc2)

    assert len(corpus.passages) == 2
    assert corpus.passages[0] == doc1
    assert corpus.passages[1] == doc2

def test_corpus_show():
    corpus = Corpus("Test Corpus")
    doc1 = "This is document 1"
    doc2 = "This is document 2"

    corpus.add(doc1)
    corpus.add(doc2)

    assert corpus.show() == [doc1, doc2]

# Add more tests for other methods of the Corpus class
