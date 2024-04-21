from utils.TableBuilder import TableBuilder
from utils.InputValidation import get_valid_range
from utils.DatabaseHelper import DatabaseHelper

def view_products():
    db_helper = DatabaseHelper()
    products = db_helper.get_all_products()

    table = TableBuilder(max_content_per_page=1000, num_column=False) \
        .add_headers(["Product Number", "Item Name", "Item Price", "Available Quantity"]) \
        .add_rows(products)

    table.build()
    return products


def select_item(products):
    prompt = "Please enter the row number of the item you want to select"
    row_num = get_valid_range(prompt, 1, len(products))
    return products[row_num -1]


def stock_main(cart):
    from views.PurchaseView import purchase_main
    stock = view_products()
    selected_item = select_item(stock)
    purchase_main(selected_item, cart)

    