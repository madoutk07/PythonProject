from Model.Author import Author

def test_author_initialization():
    author = Author("Test Author")
    assert author.name == "Test Author"
    assert author.ndoc == 0
    assert author.production == []

def test_author_add_production():
    author = Author("Test Author")
    author.add("test1")
    assert author.ndoc == 1
    assert author.production == ["test1"]

def test_author_string_representation():
    author = Author("Test")
    assert str(author) == "Auteur : Test\t# nombreproductions : 0"
