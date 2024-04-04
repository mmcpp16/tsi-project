import csv, os
from utils.TableBuilder import TableBuilder
#from src.PurchaseOptions import PurchaseOptions
from input_validation import *

class ViewStock:

    #I've kept this in from Login - happy to get rid of it if it's not needed
    def fix_working_directory(self):
        current_working_directory = os.getcwd()
        while "test" in current_working_directory or "src" in current_working_directory:
            os.chdir("../")
            current_working_directory = os.getcwd()

    def read_stock_data(self,file_name):
        self.fix_working_directory()
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
            row_num = input("Please enter the row number of the item you want to select: ")
            validate_type(row_num, "int")
            row_num = int(row_num)
            validate_range(row_num, 1, len(stock))
            return stock[row_num-1] #not sure if this implements the input validation properly?

    

    def main():
        stock = read_stock_data("shopstock.csv")
        self.display_stock(stock)
        selected_item = self.select_item(stock)
        PurchaseOptions.main(selected_item)
    
    if __name__ == "__main__":
        view_stock = ViewStock()
        view_stock.main()

    