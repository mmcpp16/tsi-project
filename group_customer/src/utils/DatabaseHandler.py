import sqlite3

class DatabaseHandler:
    dbConnection = None

    # Singleton code taken for GeeksForGeeks
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(DatabaseHandler, self).__new__(self)
        return self.instance

    def connect(self):
        if self.dbConnection is not None: return
        try:
            self.dbConnection = sqlite3.connect("../../resource/database.db")

        except sqlite3.Error as error:
            print(f"{error.sqlite_errorcode} - {error.sqlite_errorname}\nFailed connecting to the sqlite3 db.")

if __name__ == '__main__':
    database = DatabaseHandler()
    database2 = DatabaseHandler()

    print(database is database2)
    database.connect()
    database2.connect()
    print(database.dbConnection is database2.dbConnection)
    print(database.dbConnection is not None)