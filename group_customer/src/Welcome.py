class Welcome:
    def welcome(self):
        print("""
                         _____       _           _            
                        /__   \_   _| |__  _   _| | __ _ _ __ 
                          / /\/ | | | '_ \| | | | |/ _` | '__|
                         / /  | |_| | |_) | |_| | | (_| | |   
                         \/    \__,_|_.__/ \__,_|_|\__,_|_|      
                    """)
        enter = input("                    Welcome to Tubular! Press enter to continue!")
        if enter == "":
            print("Here is the stock:")
            ViewStock.Main()
        else:
            print("That's not how you enter :(")
            Welcome.welcome(self)