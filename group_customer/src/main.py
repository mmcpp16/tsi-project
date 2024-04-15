#from src.Welcome import Welcome
import Owner
import sys

class Main:
    def main():
        welcome = Welcome()
        welcome.welcome()

if __name__ == '__main__':
    if sys.argv[1] == 'owner':
        Owner.owner_main()
    # Main.main()

