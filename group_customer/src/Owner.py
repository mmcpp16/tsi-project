from datetime import datetime

from utils.TableBuilder import TableBuilder
from utils.input_validation import get_valid_range, get_valid_type
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
        .add_headers(["Product Number", "Item Name", "Available Quantity", "Item Price"]) \
        .add_rows(products)

    table.build()

    option = get_valid_range("Which product do you want to edit the quantity of? (Exit with 0)", 0, len(products))

    if option == 0:
        return owner_main()

    quantity = get_valid_type(f"What do you want to set the quantity of {products[option-1][1]} to?", int)

    cursor.execute("UPDATE Product SET quantity = ? WHERE Product.id = ?", (quantity, option))

    connection.commit()

    print("Product has been updated.")
    input("Press enter to continue...")

    owner_main()

def view_order():
    database = DatabaseHandler()
    database.connect()
    connection = database.dbConnection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CustomerOrder")
    orders = cursor.fetchall()

    order_table = TableBuilder(max_content_per_page=1000, num_column=False) \
        .add_headers(["Order ID", "First Name", "Last Name", "Passphrase", "Collection Date"]) \
        .add_rows(orders)

    order_table.build()

    answer = get_valid_range("Which order do you wish to view the products for? (0 to exit)", 0, len(orders))

    if answer == 0:
        return owner_main()

    cursor.execute("""
       SELECT Product.name ,ProductOrder.quantity, ProductOrder.rent_period, Product.full_price
       FROM ProductOrder
       INNER JOIN Product ON ProductOrder.product_id = Product.id
       WHERE ProductOrder.order_id = ?
       """, str(answer))
    products = cursor.fetchall()
    formatted_products = []
    for product in products:
        if product[2] == 0:
            formatted_products.append([*product, product[1]*product[3]])
        else:
            formatted_products.append([*product, round((product[1]/14*product[2])*product[3], 2)])
    product_table = TableBuilder(max_content_per_page=1000, num_column=False)\
        .add_headers(["Product Name", "Quantity", "Rent Period", "Unit Price", "Total Price"])\
        .add_rows(formatted_products)
    product_table.build()

    input("Press enter to continue...")
    owner_main()