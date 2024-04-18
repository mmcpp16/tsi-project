from ViewCart import view_cart
from Welcome import welcome
from utils.DatabaseHelper import DatabaseHelper
from utils.input_validation import get_valid_range


def check_out(cart):
    view_cart(cart)  # Assuming ViewCart is an array of tuples with # (ID) (Name) (Amount) (Price) (Duration)

    prompt = "Do you accept this? \n 1 = Yes \n 0 = No \n"
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
