import pytest
from Model.Classes import Document

def test_document_repr():
    doc = Document("Title", "Author", "2022-01-01", "example.com", "Lorem ipsum")
    expected_repr = "Titre : Title\tAuteur : Author\tDate : 2022-01-01\tURL : example.com\tTexte : Lorem ipsum\tType : None"
    assert repr(doc) == expected_repr

def test_document_str():
    doc = Document("Title", "Author", "2022-01-01", "example.com", "Lorem ipsum")
    expected_str = "Title, par Author"
    assert str(doc) == expected_str

def test_document_get_type():
    doc = Document()
    assert doc.getType() is None

if __name__ == "__main__":
    pytest.main()
