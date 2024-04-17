from src.ViewStock import ViewStock
def welcome():
    print("""
                        _____       _           _            
                       /__   \_   _| |__  _   _| | __ _ _ __ 
                         / /\/ | | | '_ \| | | | |/ _` | '__|
                        / /  | |_| | |_) | |_| | | (_| | |   
                        \/    \__,_|_.__/ \__,_|_|\__,_|_|      
                """)
    enter = input("Welcome to Tubular! Press enter to continue!".rjust(65))
    if enter == "":
        print("Here is the stock:")
        ViewStock.main()
    else:
        print("That's not how you enter :(")
        welcome()