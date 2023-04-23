from ..models import Author

def create_author() -> Author:
    author_name = input("Upisite ime i prezime autora: ")
    author = Author(author_name)
    return author