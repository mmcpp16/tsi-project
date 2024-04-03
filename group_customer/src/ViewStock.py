import csv, os
#from utils.TableBuilder import TableBuilder
#from src.PurchaseOptions import PurchaseOptions

class ViewStock:

    #I've kept this in from CustomerLoad - happy to get rid of it if it's not needed
    def fix_working_directory(self):
        current_working_directory = os.getcwd()
        while "test" in current_working_directory or "src" in current_working_directory:
            os.chdir("../")
            current_working_directory = os.getcwd()

    def read_stock_data(self,file_name):
        self.fix_working_directory()
        stock = []
        with open("resource/" + file_name, 'r') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                stock.append(row)
        return stock
    
    def display_stock(stock): #include utils.TableBuilder
        table_headers = ["Row Number", "Item Name", "Item Price", "Available Quantity"]
        data = [row["row_number"], row["item_name"], row["item_price"], row["available_quantity"] for row in stock]
        # table = TableBuilder.build_table(table_headers, data)

    
    def select_item(stock):
        row_num = int(input("Please enter the row number of the item you want to select: "))
        # implement input validation here?
    

    def main():
        stock = read_stock_data("shopstock.csv")
        display_stock(stock)
        selected_item = select_item(stock)
        PurchaseOptions.main(selected_item)
    
    if __name__ == "__main__":
        main()

    