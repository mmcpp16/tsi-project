from utils.DatabaseHandler import DatabaseHandler

if __name__ == '__main__':
    database = DatabaseHandler()
    database.connect()
    connection = database.db_connection
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS CustomerOrder ( id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(31) NOT NULL, last_name VARCHAR(31) NOT NULL, passphrase VARCHAR(31) NOT NULL, collection_date DATETIME NOT NULL);")
    cursor.execute("CREATE TABLE IF NOT EXISTS ProductOrder ( id INTEGER PRIMARY KEY AUTOINCREMENT, order_id INTEGER NOT NULL, product_id INTEGER NOT NULL, quantity INTEGER NOT NULL, rent_period INTEGER NOT NULL, FOREIGN KEY (order_id) REFERENCES CustomerOrder(id), FOREIGN KEY (product_id) REFERENCES Product(id));")
    cursor.execute("CREATE TABLE IF NOT EXISTS Product ( id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(31), quantity INTEGER NOT NULL, full_price DECIMAL(8, 2) NOT NULL);")

    products = [("Beach Towel", 15.99, 100),
    ("Pedal Boat", 1899.99, 10),
    ("Sunglasses", 25.50, 75),
    ("Beach Umbrella", 29.99, 30),
    ("Beach Chair", 24.99, 40),
    ("Flip Flops", 12.50, 80),
    ("Volley Ball", 19.99, 60),
    ("Surf Board (Adult)", 121.99, 25),
    ("Surf Board (Child)", 104.99, 20),
    ("Inflatable Pool Float", 18.99, 50)]

    customer_orders = [("Ayan", "Ahmad", "banana", "2024-04-26 12:00:00"),
                       ("Andrew", "Mckelvey", "abra kadabra", "2024-04-27 12:00:00"),]

    products_orders = [(1, 1, 5, 0), (1, 3, 2, 5), (1, 7, 1, 5), (1, 8, 1, 0), (1, 10, 1, 5),
                       (2, 2, 1, 0), (2, 3, 2, 5), (2, 7, 1, 5), (2, 10, 1, 5),]
    cursor.executemany("INSERT INTO CustomerOrder (first_name, last_name, passphrase, collection_date) VALUES (?, ?, ?, ?)", customer_orders)
    cursor.executemany("INSERT INTO ProductOrder (order_id, product_id, quantity, rent_period) VALUES (?, ?, ?, ?)", products_orders)
    cursor.executemany("INSERT INTO Product (name, full_price, quantity) VALUES (?, ?, ?)", products)
    connection.commit()
