from utils.TableBuilder import TableBuilder
from src.BuyOrRent import BuyOrRent
from utils.InputValidation import *
import sqlite3

class ViewStock:

    def __init__(self):
        self.db = DatabaseHandler()
        self.db.connect()

    def read_stock_data(self):
        cursor = self.db.dbConnection.cursor()
        cursor.execute("SELECT row_number, item_name, item_price, available_quantity, purchase_option FROM shopstock")
        return cursor.fetchall()
    
    def display_stock(self, stock):
        table_headers = ["Row Number", "Item Name", "Item Price", "Available Quantity", "Purchase Option"]
        data = [[row["row_number"], row["item_name"], row["item_price"], row["available_quantity"], row["purchase_option"]] for row in stock]
        table = TableBuilder()
        table.add_headers(table_headers)
        table.add_rows(data)
        table.build()

    
    def select_item(self, stock):
        prompt = "Please enter the row number of the item you want to select"
        row_num = get_valid_range(prompt, 1, len(stock))
        return stock[row_num - 1]
    

    def main(self):
        stock = self.read_stock_data()
        self.display_stock(stock)
        selected_item = self.select_item(stock)
        BuyOrRent.main(selected_item)
    
    if __name__ == "__main__":
        view_stock = ViewStock()
        view_stock.main()

    