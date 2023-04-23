
from ....project_data import DATABASE_PATH
from ...shared import bookstore_db_repo


def insert_author(author_data):
    #CREATE

    insert_table_query = '''
    INSERT INTO Authors (first_name, last_name)
    VALUES (?, ?)
    ;
    '''

    result = bookstore_db_repo(insert_table_query, author_data, "")
    return result

def select_author(id):
    #READ / RETRIEVE

    select_from_table_query = '''
    SELECT * FROM Authors
    WHERE id = ?
    ;
    '''
    result = bookstore_db_repo(select_from_table_query, id, "get")
    return result


def update_author(author_data):

    update_employees_table_query = '''
    UPDATE Authors
    SET first_name = ?, last_name = ?
    WHERE id = ?;
    '''

    result = bookstore_db_repo(update_employees_table_query, author_data, "")
    return result  

def delete_author(id):

    delete_query = '''
    DELETE FROM Authors
    WHERE id = ?
    '''
    result = bookstore_db_repo(delete_query, id, "")
    return result





