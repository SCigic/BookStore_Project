
"""
- tablice za cuvanje podataka o: 
    - autorima knjiga
    - knjigama
    - izdavacima

- relacije: 
    knjiga: 
        - svaka knjiga ima jednog autora (check)
        - svaka knjiga moze imati jednog izdavaca (check)

    autor
        - svaki autor ima vise knjiga (kolekcija knjiga) (check)
        - svaki autor ima vise izdavaca (check)

    izdavac:
        - svaki izdavac ima vise autora (check)
        - svaki izdavac ima vise knjiga (check)

"""

from sqlalchemy.orm import declarative_base, relationship, backref, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, and_

Base = declarative_base() # reprezentacija nase baze unutar naseg koda
                          # sve nase klase ce naslijediti svojstva i metode koje nudi taj objekt
                          # sve nase klase koje imaju naslijedjen Base, od njih ce biti napravljene tablice
# postoji screenshot "database_connections" (poslovni komp) gdje su bolje prikazane relacije

# region 1. korak - kreiranje tablica (unutar naše baze) pomocu Python klasa, prosirenih SQL Alchemy modulom

# ove 2 tablice su many:many, zato moramo napraviti nove JOIN tablice 

author_publisher = Table(
    "authors_publishers",
    Base.metadata,     ## povezujemo tablicu s SQLAlchemy da mozemo raditi s njom
    Column("id", Integer, primary_key=True),
    Column("author.id", Integer, ForeignKey("authors.id")),
    Column("publisher.id", Integer, ForeignKey("publishers.id"))

)

book_publisher = Table(
    "books_publishers", 
    Base.metadata, 
    Column("id", Integer, primary_key=True), 
    Column("book.id", Integer, ForeignKey("books.id")), 
    Column("publisher.id", Integer, ForeignKey("publishers.id"))
)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False) # nullable -> NOT NULL ili NULL
    last_name = Column(String(150), nullable=False)

    #relacije - ovo nije dio SQLa i nije mandatory
    # jedan autor moze imati vise knjiga (kolekciju)
    books = relationship("Book", backref=backref("author")) # .author ce se pojaviti kao metoda u objektu klase Book
                                                             # da nemamo to, mogli bi koristiti samo metodu .author_id
                                                             # kod objekta klase Author, pozivamo metodu .books

    publishers = relationship("Publisher", secondary=author_publisher, back_populates="authors")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"))

    publishers = relationship("Publisher", secondary=book_publisher, back_populates="books")


class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)

    #relacije : svaki publisher ima vise autora i vise knjiga
    authors = relationship("Author", secondary=author_publisher, back_populates="publishers")
    books = relationship("Book", secondary=book_publisher, back_populates="publishers")

#endregion

# region 2. korak - kreiranje baze s tablicama

#kreiramo stroj koji ce nam omoguciti da se povezemo s bazom
db_engine = create_engine("sqlite:///db_files/book_store.db")
Base.metadata.create_all(db_engine)

#endregion

# region 3. korak - koristenje baze (slicno kao cursor)

Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

#endregion


book_title = "The Stand"
author_name = "Stephan King"
publisher_name = "Random House Ltd."

author_name_parts = author_name.split(" ")
author_first_name = author_name_parts[0]
author_last_name = author_name_parts[1]

#moze i ovako: 
#author_first_name, _, author_last_name = author_name.partition(" ")

# ne mozemo nista dodati bez provjere u bazu!
# ako vec postoji knjiga u bazi xx, autora yy i izdavaca zz, vratit će mi tu knjigu; ako nema, dobit cemo none
book = (
    session.query(Book)     #SELECT * FROM books
    .join(Author)
    .filter(Book.title == book_title)
    .filter(
    and_(Author.first_name == author_first_name, Author.last_name == author_last_name))
    .filter(Book.publishers.any(Publisher.name == publisher_name))
    .one_or_none()
)

# ako toga nema u bazi, idemo to kreirati
if book == None: 
    book = Book(title = book_title)

author = (
    session.query(Author)
    .filter(and_(Author.first_name == author_first_name, Author.last_name == author_last_name))
    .one_or_none()
)

if author == None: 
    author = Author(first_name = author_first_name, last_name = author_last_name)
    session.add(author)


publisher = (
    session.query(Publisher)
    .filter(Publisher.name == publisher_name)
    .one_or_none
)

if publisher == None: 
    publisher = Publisher(name = publisher_name)
    publisher.authors.append(author)
    session.add(publisher)

book.author = author
book.publishers.append(publisher)
session.add(book)


session.commit()