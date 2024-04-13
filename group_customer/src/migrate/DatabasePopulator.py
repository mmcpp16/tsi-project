from utils.DatabaseHandler import DatabaseHandler

if __name__ == '__main__':
    database = DatabaseHandler()
    database.connect()
    connection = database.dbConnection
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS CustomerOrder ( id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(31), last_name VARCHAR(31), passphrase VARCHAR(31), collection_date DATETIME);")
    cursor.execute("CREATE TABLE IF NOT EXISTS ProductOrder ( id INTEGER PRIMARY KEY AUTOINCREMENT, order_id INTEGER NOT NULL, product_id INTEGER NOT NULL, quantity INTEGER NOT NULL, FOREIGN KEY (order_id) REFERENCES CustomerOrder(id), FOREIGN KEY (product_id) REFERENCES Product(id));")
    cursor.execute("CREATE TABLE IF NOT EXISTS Product ( id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(31), quantity INTEGER, full_price DECIMAL(8, 2) );")

    products = [("Beach Towel", 15.99, 100),
    ("Sunscreen SPF 50", 8.99, 50),
    ("Sunglasses", 25.50, 75),
    ("Beach Umbrella", 29.99, 30),
    ("Beach Chair", 24.99, 40),
    ("Flip Flops", 12.50, 80),
    ("Volley Ball", 19.99, 60),
    ("Surf Board (Adult)", 121.99, 25),
    ("Surf Board (Child)", 104.99, 20),
    ("Inflatable Pool Float", 18.99, 50)]

    cursor.executemany("INSERT INTO Product (name, full_price, quantity) VALUES (?, ?, ?)", products)
    connection.commit()