from src.ViewStock import ViewStock
from utils.InputValidation import *
from src.ViewCart import view_cart

class BuyOrRent(selected_item):
    def buy_or_rent(self,selected_item):
        purchase_quantity = get_valid_range("Enter desired quantity", 1, selected_item[1])
        purchase_method = get_valid_range("Enter 1 to buy or 2 to rent",1,2)
        if purchase_method == 1:
            self.add_to_cart(selected_item[0], purchase_quantity, selected_item[3])
            view_cart_or_continue
        elif purchase_method == 2:
            purchase_duration = get_valid_range("How many days would you like to rent for? Choose between 1 and 7 days.", 1, 7)
            self.add_to_cart(selected_item[0], purchase_quantity,selected_item[3],purchase_duration)
            view_cart_or_continue

    def add_to_cart(self, selected_item[0], purchase_quantity, selected_item[3], purchase_duration=0):
        if purchase_duration != 0:
            selected_item[3] = selected_item[3] / 14 * purchase_duration
        cart = [selected_item[0], purchase_quantity, selected_item[3], purchase_duration]
        view_cart.cart.append(cart)
        print("Added to cart")

def view_cart_or_continue():

    choice = get_valid_range("Enter 1 to continue shopping or 2 to view cart",1,2)
        if choice == 1:
            ViewStock.main()
        elif choice == 2:
            ViewCart.view_cart()
