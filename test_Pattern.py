from Model import DocumentGenerator
from Model import RedditDocument, ArxivDocument
def  test_document_generator_init():

    doc_1 = DocumentGenerator.factory("Title", "Author", "2022-01-01", "https://example.com", "Sample text" ,nbcommentaires = 10)
    doc_2 = DocumentGenerator.factory("Title", "Author", "2022-01-01", "https://example.com", "Sample text", co_auteurs = ["me","you"])
    # print(type(doc_1), type(doc_2))
    assert type(doc_1) == RedditDocument
    assert type(doc_2) == ArxivDocument
