import Owner
import sys
from src.Welcome import welcome

class Main:
    def main():
        welcome()

if __name__ == '__main__':
    if sys.argv[1] == 'owner':
        Owner.owner_main()
    Main.main()

