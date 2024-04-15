from datetime import datetime

from utils.TableBuilder import TableBuilder
from utils.input_validation import get_valid_range
from utils.DatabaseHandler import DatabaseHandler

def owner_main():
    print("Welcome to the Owner View!\n"
          "[1] View/Alter Product Stock\n"
          "[2] View orders\n")
    answer = get_valid_range("What do you want to view?", 1, 2)
    if answer == 1:
        view_products()
    elif answer == 2:
        view_order()

def view_products():
    database = DatabaseHandler()
    database.connect()
    connection = database.dbConnection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()

    table = TableBuilder(max_content_per_page=1000, num_column=False) \
        .add_headers(["Product Number", "Item Name", "Item Price", "Available Quantity"]) \
        .add_rows(products)

    table.build()

def view_order():
    database = DatabaseHandler()
    database.connect()
    connection = database.dbConnection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CustomerOrder")
    orders = cursor.fetchall()

    formatted_orders = [(order[0], order[1], order[2], order[3], datetime.fromtimestamp((order[4] / 1000))) for order in orders]

    order_table = TableBuilder(max_content_per_page=1000, num_column=False) \
        .add_headers(["Order ID", "First Name", "Last Name", "Passphrase", "Collection Date"]) \
        .add_rows(formatted_orders)

    order_table.build()

    answer = get_valid_range("Which order do you wish to view the products for?", 0, len(orders))

    cursor.execute("""
       SELECT Product.name, ProductOrder.quantity, Product.full_price
       FROM ProductOrder
       INNER JOIN Product ON ProductOrder.product_id = Product.id
       WHERE ProductOrder.order_id = ?
       """, str(answer))
    products = cursor.fetchall()

    product_table = (TableBuilder(max_content_per_page=1000, num_column=False)
        .add_headers(["Product Name", "Quantity", "Price"])
        .add_rows(products))
    # Need to add: rental period and do total price equation
    product_table.build()