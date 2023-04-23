
from features import (create_author,
                      init_db_tables)



def start_app():

    # create table in DB
    init_db_tables()
    
    book_author = create_author()
    print(book_author)

if __name__ == "__main__":
    start_app()
