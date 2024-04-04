import csv
from utils.TableBuilder import TableBuilder
#from src.PurchaseOptions import PurchaseOptions
from utils.InputValidation import *

class ViewStock:

    def read_stock_data(self,file_name):
        stock = []
        with open("resource/" + file_name, 'r') as file:
            file_reader = csv.DictReader(file)
            for row in file_reader:
                stock.append(row)
        return stock
    
    def display_stock(self, stock):
        table_headers = ["Row Number", "Item Name", "Item Price", "Available Quantity", "Purchase Option"]
        data = [[row["row_number"], row["item_name"], row["item_price"], row["available_quantity"], row["purchase_option"]] for row in stock]
        table = TableBuilder()
        table.add_headers(table_headers)
        table.add_rows(data)
        table.build()

    
    def select_item(stock):
        while True:
            prompt = "Please enter the row number of the item you want to select"
            row_num = get_valid_range(prompt, 1, len(stock))
            return stock[row_num - 1]
    

    def main(self):
        stock = self.read_stock_data("shopstock.csv")
        self.display_stock(stock)
        selected_item = self.select_item(stock)
        #PurchaseOptions.main(selected_item)
    
    if __name__ == "__main__":
        view_stock = ViewStock()
        view_stock.main()

    