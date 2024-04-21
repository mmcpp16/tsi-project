from ViewCart import view_cart
from Welcome import welcome
from utils.DatabaseHelper import DatabaseHelper
from utils.input_validation import get_valid_range


def check_out(cart):
    prompt = "Do you accept this price? \n [1] Yes \n [0] No"
    choice = get_valid_range(prompt, 0, 1)

    if choice == 1:
        print("Great! We will need some of your info, including a pass phrase.\n(this will be needed at the pick up "
              "desk)")
        first_name = input("what is your first name? \t: ")
        last_name = input("what is your last name? \t: ")
        pass_phrase = input("what is your pass phrase \t: ")
        collect_time = "2024-04-26 12:00:00"  # temporary implementation

        add_data = DatabaseHelper()
        new_cart = []
        # Takes in (Item ID, Quantity, Duration)
        for item in cart:
            new_cart.append(
                (item[0], item[2], item[4])
            )

        add_data.add_customer_order(first_name, last_name, pass_phrase, collect_time, new_cart)
        
        database = DatabaseHandler()
        database.connect()
        connection = database.dbConnection
        cursor = connection.cursor()

        for cart_item in new_cart:
            cursor.execute("SELECT quantity FROM Product WHERE Product.id = ?", (str(cart_item[0])))
            quantity = cursor.fetchone()
            cursor.execute("UPDATE Product SET quantity = ? WHERE Product.id = ?", (quantity[0] - cart_item[1], cart_item[0]))
            connection.commit()
        
        print(f"Thanks {first_name}! Make sure to use the phrase \"{pass_phrase}\" at the pick up desk!")
    else:
        print("Sorry we couldn't accommodate you.")

    input("Press enter to return home")
    welcome()


# Example usecase
# if __name__ == '__main__':
#     the_cart = [
#         [0, "Beach Towel", 100, 15.99, 0],
#         [1, "Sunscreen SPF 50", 50, 8.99, 0],
#         [2, "Sunglasses", 75, 25.50, 7],
#         [3, "Beach Umbrella", 30, 29.99, 4],
#         [4, "Beach Chair", 40, 24.99, 7],
#     ]
#     check_out(the_cart)
