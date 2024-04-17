from utils.TableBuilder import *


def view_cart(cart):  # assuming cart is a list of items
    cart_table = TableBuilder(num_column=False)
    headers = ["Item Name", "Price", "Quantity", "Duration"]
    cart_table.add_headers(headers)

    formatted_cart = [(item[0], item[1], item[2], "Life" if item[3] == 0 else item[3]) for item in cart]

    cart_table.add_rows(formatted_cart)
    cart_table.build()

    subtotal = 0
    for item in cart:
        subtotal = subtotal + (item[1] * item[2])  # will be changed to .price and .quantity when ready

    print(f"Your subtotal is £{subtotal:,.2f}")


if __name__ == '__main__':
    thecart = [
        ["Beach Towel", 15.99, 100, 0],
        ["Sunscreen SPF 50", 8.99, 50, 0],
        ["Sunglasses", 25.50, 75, 7],
        ["Beach Umbrella", 29.99, 30, 4],
        ["Beach Chair", 24.99, 40, 7],
        ["Flip Flops", 12.50, 80, 2],
        ["Volley Ball", 19.99, 60, 1],
        ["Surf Board (Adult)", 121.99, 25, 1],
        ["Surf Board (Child)", 104.99, 20, 1],
        ["Inflatable Pool Float", 18.99, 50, 7]
    ]
    view_cart(thecart)
