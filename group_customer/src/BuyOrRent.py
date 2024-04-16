from src.ViewStock import ViewStock
from utils.InputValidation import *
from Cart.viewcart import ViewCart
#if product can be bought or rented ask if they want to buy or rent
class BuyOrRent:
    def buy_or_rent(self):
        purchase_quantity = get_valid_range("Enter desired quantity", 1, 9)  # where 9 is a dummy value
        purchase_method = get_valid_range("Enter 1 to buy or 2 to rent",1,2)
        if purchase_method == 1:
            #todo override current cart
            self.add_to_cart(itemname, purchase_quantity, itemprice)#where itemname and itemprice are dummys
            self.continue_or_view_cart()
        elif purchase_method == 2:
            purchase_duration = get_valid_range("How many days would you like to rent for? Choose between 1 and 7 days.", 1, 7)
            self.add_to_cart(itemname, purchase_quantity, itemprice,purchase_duration)  # where itemname and itemprice are dummys
            self.continue_or_view_cart()

    def add_to_cart(self,itemname,itemquantity,itemprice,rent_duration=14):
        itemlist = [itemname, itemquantity, itemprice, rent_duration]
        ViewCart.cart.append(itemlist)
        print("Added to cart!")

    def continue_or_view_cart():
        choice = get_valid_range("Enter 1 to continue shopping or 2 to view cart",1,2)
        if choice == 1:
            ViewStock.main()
        elif choice == 2:
            ViewCart.view_cart()
