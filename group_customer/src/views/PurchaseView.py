from utils.InputValidation import get_valid_range
from views.StockView import stock_main
from views.CartView import cart_main


def purchase_main(selected_item, cart):
    purchase_quantity = get_valid_range("Enter desired quantity", 1, selected_item[2])
    purchase_method = get_valid_range("Enter 1 to buy or 2 to rent",1,2)
    if purchase_method == 1:
        add_to_cart(cart, selected_item[0], selected_item[1], purchase_quantity, selected_item[3])
        view_cart_or_continue(cart)
    elif purchase_method == 2:
        purchase_duration = get_valid_range("How many days would you like to rent for? Choose between 1 and 7 days.", 1, 7)
        add_to_cart(cart, selected_item[0],selected_item[1],purchase_quantity,selected_item[3],purchase_duration)
        view_cart_or_continue(cart)

def add_to_cart(cart, id, name, purchase_quantity, price, purchase_duration=0):
    if purchase_duration != 0:
        price = price / 14 * purchase_duration
    cart.append([id,name, purchase_quantity, price, purchase_duration])
    print("Added to cart")
    return cart

def view_cart_or_continue(cart):
    choice = get_valid_range("Enter 1 to continue shopping or 2 to view cart",1,2)
    if choice == 1:
        stock_main(cart)
    elif choice == 2:
        cart_main(cart)