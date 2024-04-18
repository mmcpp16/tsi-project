from utils.TableBuilder import *


def view_cart(cart):  # Assuming Cart is an array of tuples with # (ID) (Name) (Amount) (Price) (Duration)
    cart_table = TableBuilder(num_column=False)
    headers = ["Item Name", "Quantity", "Price", "Duration"]
    cart_table.add_headers(headers)

    formatted_cart = [(item[1], item[2], item[3], "Life" if item[4] == 0 else item[3]) for item in cart]

    cart_table.add_rows(formatted_cart)
    cart_table.build()

    subtotal = 0
    for item in cart:
        subtotal = subtotal + (item[3] * item[2])

    print(f"Your subtotal is £{subtotal:,.2f}")


#UseCase
# if __name__ == '__main__':
#     the_cart = [
#         [1, "Beach Towel", 100, 15.99, 0],
#         [2, "Sunscreen SPF 50", 50, 8.99, 0],
#         [3, "Sunglasses", 75, 25.50, 7],
#         [4, 'Beach Umbrella', 30, 29.99, 4],
#     ]
#     view_cart(the_cart)
