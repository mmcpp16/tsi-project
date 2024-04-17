from utils.TableBuilder import *


def view_cart(cart):  # assuming cart is a list of items
    cart_table = TableBuilder(num_column=False)
    headers = ["Item Name", "Price", "Quantity"]
    cart_table.add_headers(headers)
    cart_table.add_rows(cart)
    cart_table.build()

    subtotal = 0
    for item in cart:
        subtotal = subtotal + (item[1] * item[2])  # will be changed to .price and .quantity when ready

    print(f"Your subtotal is £{subtotal:,.2f}")


if __name__ == '__main__':
    thecart = [
        ["Beach Towel", 15.99, 100],
        ["Sunscreen SPF 50", 8.99, 50],
        ["Sunglasses", 25.50, 75],
        ["Beach Umbrella", 29.99, 30],
        ["Beach Chair", 24.99, 40],
        ["Flip Flops", 12.50, 80],
        ["Volley Ball", 19.99, 60],
        ["Surf Board (Adult)", 121.99, 25],
        ["Surf Board (Child)", 104.99, 20],
        ["Inflatable Pool Float", 18.99, 50]
    ]
    view_cart(thecart)
