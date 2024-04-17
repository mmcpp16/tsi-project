from ViewCart import view_cart
from Welcome import welcome
from utils.input_validation import get_valid_range


def check_out(cart):
    view_cart(cart)  # Assuming ViewCart uses table builder and takes in a list of 'item' objects

    prompt = "Do you accept this? \n 1 = Yes \n 0 = No \n"
    choice = get_valid_range(prompt, 0, 1)

    if choice == 1:
        print("Great! We will need some of your info, including a pass phrase.\n(this will be needed at the pick up "
              "desk)")
        first_name = input("what is your first name? \t: ")
        last_name = input("what is your last name? \t: ")
        pass_phrase = input("what is your pass phrase \t: ")

        collect_time = "2024-04-26 12:00:00"  # temporary implementation

        data_entry = (first_name, last_name, pass_phrase, collect_time)
        #Not sure how to add to database from here, should that be an external function?

        print(f"Thanks {first_name}! Make sure to use the phrase \"{pass_phrase}\" at the pick up desk!")
    else:
        print("Sorry we couldn't accommodate you.")

    input("Press enter to return home")
    welcome()

# Example usecase
# if __name__ == '__main__':
#     the_cart = [
#         ["Beach Towel", 15.99, 100, 0],
#         ["Sunscreen SPF 50", 8.99, 50, 0],
#         ["Sunglasses", 25.50, 75, 7],
#         ["Beach Umbrella", 29.99, 30, 4],
#         ["Beach Chair", 24.99, 40, 7],
#         ["Flip Flops", 12.50, 80, 2],
#         ["Volley Ball", 19.99, 60, 1],
#         ["Surf Board (Adult)", 121.99, 25, 1],
#         ["Surf Board (Child)", 104.99, 20, 1],
#         ["Inflatable Pool Float", 18.99, 50, 7]
#     ]
#     check_out(the_cart)
