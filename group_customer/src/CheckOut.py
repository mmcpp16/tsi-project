from ViewCart import *
from Welcome import *
from utils.input_validation import *


def check_out(cart):
    ViewCart(cart)  # Assuming ViewCart uses table builder and takes in a list of 'item' objects

    subtotal = 0
    for item in cart:
        subtotal += item.price
    prompt = f"Your subtotal is £{subtotal:,.2f} Do you accept this? \n 1 = Yes \n 0 = No"
    choice = get_valid_range(prompt, 0, 1)

    if choice == 1:
        print("great! Please create a password.\n(this will be needed at the pick up desk)")
        password = input("Password: ")

        print(f"Make sure to use the phrase \"{password}\" at the pick up desk!")
    else:
        print("Sorry we couldn't accommodate you")

    input("Press enter to return home")
    Welcome.welcome()