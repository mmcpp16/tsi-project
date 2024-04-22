from utils.DatabaseHandler import DatabaseHandler


class DatabaseHelper:
    connection = None
    cursor = None

    def __init__(self):
        database = DatabaseHandler()
        database.connect()
        self.connection = database.db_connection
        self.cursor = self.connection.cursor()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM Product")
        return self.cursor.fetchall()

    def get_all_customer_orders(self):
        self.cursor.execute("SELECT * FROM CustomerOrder")
        return self.cursor.fetchall()

    def get_customer_products(self, order_id):
        self.cursor.execute("""
              SELECT Product.name ,ProductOrder.quantity, ProductOrder.rent_period, Product.full_price
              FROM ProductOrder
              INNER JOIN Product ON ProductOrder.product_id = Product.id
              WHERE ProductOrder.order_id = ?
              """, order_id)
        return self.cursor.fetchall()

    def add_customer_order(self, first_name, last_name, passphrase, collection_date, products):
        self.cursor.execute(
            "INSERT INTO CustomerOrder (first_name, last_name, passphrase, collection_date) VALUES (?, ?, ?, ?)",
            [first_name, last_name, passphrase, collection_date])
        customer_order_id = self.cursor.lastrowid

        self.cursor.executemany("INSERT INTO ProductOrder (order_id, product_id, quantity, rent_period) VALUES (?, ?, ?, ?)", [(customer_order_id, *product) for product in products])
        self.connection.commit()

    def set_stock_quantity(self, product_id, quantity):
        self.cursor.execute("UPDATE Product SET quantity = ? WHERE Product.id = ?", (quantity, product_id))
        self.connection.commit()

    def update_quantity_on_order(self, cart):
        for cart_item in cart:
            self.cursor.execute("SELECT quantity FROM Product WHERE Product.id = ?", (str(cart_item[0])))
            quantity = self.cursor.fetchone()
            self.cursor.execute("UPDATE Product SET quantity = ? WHERE Product.id = ?",
                           (quantity[0] - cart_item[1], cart_item[0]))
            self.connection.commit()

if __name__ == '__main__':
    database = DatabaseHelper()
    database.add_customer_order("Ayan", "Ahmad", "Banana", "2024-04-27 12:00:00", [(1, 5, 0), (3, 2, 5), (7, 1, 5), (8, 1, 0), (10, 1, 5)])