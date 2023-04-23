
import sqlite3
from project_data import DATABASE_PATH


def bookstore_db_repo(db_query, query_data = None, db_action= ""):


    try:
        sqlConnection = sqlite3.connect(DATABASE_PATH)
        cursor = sqlConnection.cursor()

        if query_data != None: 
            cursor.execute(db_query, query_data)
            if db_action == "get":
                record_set = cursor.fetchall()
                return record_set
            else:
                sqlConnection.commit()
                cursor.close()
                return f"Uspjesno je izvrsena akcija"
        
        else:
            cursor.execute(db_query)
            sqlConnection.commit()
            cursor.close()
            return f"Uspjesno je izvrsena akcija"


    except sqlite3.Error as sql_error:
        return f"Dogodila se SQL greska {sql_error}"

    except Exception as ex:
        return f"Dogodila se greska {ex}"

    finally:
        # Na kraju zatvorimo konekciju prema bazi
        if sqlConnection:
            sqlConnection.close()   


def init_db_tables():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Authors (
    id INTEGER PRIMARY KEY
    first_name TEXT NOT NULL
    last_name TEXT NOT NULL
    );
    """
    bookstore_db_repo(create_table_query, query_data=None, db_action="")