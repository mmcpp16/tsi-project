from utils.TableBuilder import TableBuilder
from utils.input_validation import *
from utils.DatabaseHandler import DatabaseHandler
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
    return products


def select_item(products):
    prompt = "Please enter the row number of the item you want to select"
    row_num = get_valid_range(prompt, 1, len(products))
    return products[row_num -1]


def main(cart):
    from src.BuyOrRent import buy_or_rent
    stock = view_products()
    selected_item = select_item(stock)
    buy_or_rent(selected_item, cart)
    
if __name__ == "__main__":
    main()

    