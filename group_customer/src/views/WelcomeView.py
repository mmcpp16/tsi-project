from views.StockView import stock_main
def welcome():
    print(r"""
                        _____       _           _            
                       /__   \_   _| |__  _   _| | __ _ _ __ 
                         / /\/ | | | '_ \| | | | |/ _` | '__|
                        / /  | |_| | |_) | |_| | | (_| | |   
                        \/    \__,_|_.__/ \__,_|_|\__,_|_|      
                """)
    input("Welcome to Tubular! Press enter to continue!".rjust(65))
    print("Here is the stock:")
    cart = []
    stock_main(cart)
