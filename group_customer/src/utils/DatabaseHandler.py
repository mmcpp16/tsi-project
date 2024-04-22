import os
import sqlite3

class DatabaseHandler:
    db_connection = None

    # Singleton code taken for GeeksForGeeks
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(DatabaseHandler, self).__new__(self)
        return self.instance

    def connect(self):
        if self.db_connection is not None: return
        try:
            main_dir = os.path.dirname(os.path.abspath(__file__))
            resource_dir = os.path.normpath(os.path.join(main_dir, "../../resource"))
            db_path = os.path.join(resource_dir, "database.db")
            self.db_connection = sqlite3.connect(db_path)

        except sqlite3.Error as error:
            print(f"{error.sqlite_errorcode} - {error.sqlite_errorname}\nFailed connecting to the sqlite3 db.")

if __name__ == '__main__':
    database = DatabaseHandler()
    database2 = DatabaseHandler()

    print(database is database2)
    database.connect()
    database2.connect()
    print(database.db_connection is database2.db_connection)
    print(database.db_connection is not None)