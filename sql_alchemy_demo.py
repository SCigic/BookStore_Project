

from sqlalchemy.orm import declarative_base, relationship, backref, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, and_

Base = declarative_base()

#kreiramo tabelu u bazi ali ne preko SQL jezika neko preko Pythona s sqlAlchemy
"""CREATE TABLE IF NOT EXISTS Author (
    id INTEGER PRIMARY KEY
    first_name TEXT NOT NULL
    last_name TEXT NOT NULL
    );
    """

# Python klasa koja nema __init__
# kreiramo nasu tabelu tako da kreiramo klasu
# jedan objekt koji je nastao na osnovu klase predstavlja jedan red u tabeli

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)                  #1
    first_name = Column(String(150), nullable=False)        #Tin
    last_name = Column(String(150), nullable=False)         #Ujevic

    books = relationship("Book", backref=backref("author")) #koristi naziv "author" kao referencu (npr book1.author)
                                                            #[Zbirka pjesama, ...]


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)                  #1
    title= Column(String(250), nullable=False)              # Zbirka Pjesama
    author_id = Column(Integer, ForeignKey("authors.id"))   #1 -> Tin Ujevic


db_engine = create_engine("sqlite:///PyBookShop.db")
Base.metadata.create_all(db_engine)                         #u gornjoj bazi, kreiraj gore definirane tablice koje nasljeđuju Base

#isto kao cursor u sqlite
Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

book_title = "Zbirka pjesama"
book_author_first_name = "Tin"
book_author_last_name = "Ujevic"

book = (
    session.query(Book)                                     #dohvati sve iz klase Book
    .join(Author)
    .filter(Book.title == book_title)
    .filter(and_(
    Author.first_name == book_author_first_name,
    Author.last_name == book_author_last_name)
    )
    .one_or_none()
)

author = (
    session.query(Author)
    .filter(
        and_(
            Author.first_name == book_author_first_name,
            Author.last_name == book_author_last_name
        )
    )
    .one_or_none()
)

if book == None: 
    book = Book(title = book_title)

if author == None: 
    author = Author(first_name = book_author_first_name, 
                    last_name = book_author_last_name)
    session.add(author)

book.author = author
session.add(book)

session.commit()