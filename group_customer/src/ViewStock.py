from utils.TableBuilder import TableBuilder
from src.BuyOrRent import BuyOrRent
from utils.InputValidation import *
from utils.DatabaseHandler import DatabaseHandler

class ViewStock:

    def __init__(self):
        self.db = DatabaseHandler()
        self.db.connect()


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

    
    def select_item(self, stock):
        prompt = "Please enter the row number of the item you want to select"
        row_num = get_valid_range(prompt, 1, len(products))
        return stock[row_num]
    

    def main(self):
        stock = self.read_stock_data()
        self.display_stock(stock)
        selected_item = self.select_item(stock)
        BuyOrRent.main(selected_item)
    
    if __name__ == "__main__":
        view_stock = ViewStock()
        view_stock.main()

    